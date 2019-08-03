from rest_framework import generics
from .models import Projects
from .serializers import ProjectsSerializer


class ListProjectsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class ListProjectDetailsView(generics.ListAPIView):
    """
    Provides the project details
    """
    serializer_class = ProjectsSerializer
    def get_queryset(self):
        projectTitle = self.kwargs['title']
        return Projects.objects.filter(title=projectTitle)
