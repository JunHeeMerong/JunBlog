from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=200,unique=True,allow_unicode=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "categories"

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')  
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    click = models.IntegerField(null=True, default=0) # 클릭
    category = models.ForeignKey(Category,null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title}'
    
    class Meta:
        db_table = 'post'

def image_upload_path(instance, filename):
    # title = instance.post.title
    # slug = slugify(title)
    # return "post_images/%s-%s" % (slug, filename)
    return f'{instance.post.id}/{filename}'

class PostImage(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to=image_upload_path)

    def __int__(self):
        return self.id
    # 이미지크기 가로 700픽셀
    class Meta:
        db_table = 'post_image'

class PostImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = PostImage
        fields = ['image']

class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)