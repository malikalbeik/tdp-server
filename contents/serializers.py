from rest_framework import serializers
from .models import Content
import os

class ContentSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Content
        fields = '__all__'
    def get_image(self, obj):
        imagePath = str(obj.image)
        imagePath = imagePath.split('/')
        if (imagePath[0] == "tdpServer"):
            del imagePath[0]
        imagePath = str(os.path.join(*imagePath)) 
        return imagePath
