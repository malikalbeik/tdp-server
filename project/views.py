from rest_framework import generics
from .models import Projects
from .serializers import ProjectsSerializer


class ListProjectsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
