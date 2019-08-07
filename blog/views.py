from rest_framework import generics
from .models import Post, Image
from .serializers import PostSerializer
from rest_framework import viewsets, permissions

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
