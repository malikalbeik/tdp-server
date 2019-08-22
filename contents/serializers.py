from rest_framework import serializers
from .models import Content


class ContentSerializer(serializers.ModelSerializer):
    image = serializers.CharField()
    class Meta:
        model = Content
        fields = '__all__'
