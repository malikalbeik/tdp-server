from .models import Projects
from .serializers import ProjectsSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, permissions


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    def retrieve(self, request, pk=None):
        # retrieve post by title
        project = get_object_or_404(self.get_queryset().filter(title=pk))
        serializer = self.get_serializer(project)
        return Response(serializer.data)
