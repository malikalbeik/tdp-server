from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets, permissions

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_post(self, request, pk=None):
        try:  # retrieve post by slug
            return get_object_or_404(self.get_queryset().filter(slug=pk))
        except:  # retrieve post by Projects title
            return self.get_queryset().filter(project__title=pk)

    def get_queryset(self):
        if self.request.auth:
            return Post.objects.all()
        else:
            return Post.visible.all()

    def retrieve(self, request, pk=None):
        post = self.get_post(request, pk)
        serializer = self.get_serializer(post, many=True)
        return Response(serializer.data)