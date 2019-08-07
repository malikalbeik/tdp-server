from rest_framework import serializers
from .models import Post, Image

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.CharField(read_only=True)

    class Meta:
        model = Image
        fields = ('image',)


class PostSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_images(self, post):
        images = Image.objects.filter(post_id=post.id)
        serializer = ImageSerializer(images, many=True)
        return serializer.data
