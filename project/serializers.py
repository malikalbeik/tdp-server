from rest_framework import serializers
from .models import Projects
import os

class ProjectsSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()
    backgroundImage = serializers.SerializerMethodField()
    class Meta:
        model = Projects
        fields = '__all__'
    def get_backgroundImage(self, obj):
        imagePath = str(obj.backgroundImage)
        imagePath = imagePath.split('/')
        if (imagePath[0] == "tdpServer"):
            del imagePath[0]
        imagePath = str(os.path.join(*imagePath)) 
        return imagePath
    def get_logo(self, obj):
        imagePath = str(obj.logo)
        imagePath = imagePath.split('/')
        if (imagePath[0] == "tdpServer"):
            del imagePath[0]
        imagePath = str(os.path.join(*imagePath))
        return imagePath
