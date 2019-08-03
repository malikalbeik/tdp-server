from django.urls import path
from project import views


urlpatterns = [
    path('projects/', views.ListProjectsView.as_view(), name="projects-all"),
    path('projects/<slug:title>/', views.ListProjectDetailsView.as_view(), name="project-details")
]
