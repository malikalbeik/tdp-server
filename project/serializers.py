from rest_framework import serializers
from .models import Projects


class ProjectsSerializer(serializers.ModelSerializer):
    logo = serializers.CharField()
    backgroundImage = serializers.CharField()
    class Meta:
        model = Projects
        fields = '__all__' 
