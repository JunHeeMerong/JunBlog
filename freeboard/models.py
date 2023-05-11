from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class FreePost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='free_author_question')  
    content = RichTextUploadingField(blank=True,null=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    click = models.IntegerField(null=True, default=0) # 클릭

    def __str__(self):
        return f'[{self.pk}]{self.title}'
    
    class Meta:
        db_table = 'freepost'

#이미지 저장 루트
def image_upload_path(instance, filename):
    id = instance.freepost.id
    slug = slugify(id)
    return "free_post_images/%s/%s" % (slug, filename)

class FreePostImage(models.Model):
    id = models.AutoField(primary_key=True)
    freepost = models.ForeignKey(FreePost, on_delete=models.CASCADE, related_name='freeimage')
    freeimage = models.ImageField(upload_to=image_upload_path)

    def __int__(self):
        return self.id
    # 이미지크기 가로 700픽셀
    class Meta:
        db_table = 'free_post_image'

class FreePostImageSerializer(serializers.ModelSerializer):
    freeimage = serializers.ImageField(use_url=True)

    class Meta:
        model = FreePostImage
        fields = ['freeimage']

class FreeComment(models.Model):
    freepost = models.ForeignKey(FreePost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='free_author_answer')
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)