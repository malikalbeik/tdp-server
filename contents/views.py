from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from . import models, serializers


class ContentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerializer
    filter_backends = (SearchFilter, )
    search_fields = ('title', 'text', )

    def retrieve(self, request, pk=None):
        content = get_object_or_404(self.get_queryset().filter(slug=pk))
        serializer = self.get_serializer(content)
        return Response(serializer.data)
