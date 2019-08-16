from rest_framework import generics
from .models import Post, Image
from .serializers import PostSerializer
from rest_framework import viewsets, permissions

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ListProjectPostsView(generics.ListAPIView):
    """
    Provides the project details
    """
    serializer_class = PostSerializer

    def get_queryset(self):
        postSlug = self.kwargs['postSlug']
        return Post.objects.filter(slug=postSlug)
