from rest_framework import serializers
from .models import Post, Image
from project.serializers import ProjectsSerializer
from project.models import Projects

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.CharField(read_only=True)

    class Meta:
        model = Image
        fields = ('image',)


class PostSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    project = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_images(self, post):
        images = Image.objects.filter(post_id=post.id)
        serializer = ImageSerializer(images, many=True)
        return serializer.data


    def get_project(self, post):
        project = post.project
        serializer = ProjectsSerializer(project, many=False)
        return serializer.data
