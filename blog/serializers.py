from rest_framework import serializers
from models import PostImage, Post

class PostImageSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(use_url=True)

    def get_images(self, obj):
        image = obj.postimage_set.all()
        return PostImageSerializer(instance=image, many=True).data
    
    class Meta:
        model = PostImage
        fields = ['image']

    def create(self, validated_data):
        instance = Post.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            PostImage.objects.create(post=instance, image=image_data)
        return instance

class PostSerializer(serializers.ModelSerializer):

    images = PostImageSerializer(many=True, read_only=True)


    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'create_date', 'images']
        
        
    def create(self, validated_data):
        instance = Post.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            PostImage.objects.create(post=instance, image=image_data)
        return instance