
from django.urls import path
from .views import PostViewSet, ListProjectPostsView, ListPostsByProjectView


urlpatterns = [
    path('posts/', PostViewSet.as_view({'get': 'list'}), name="posts-all"),
    path('posts/<slug:projectTitle>/',
         ListProjectPostsView.as_view(), name="project-posts"),
    path('posts/<slug:postSlug>/',
         ListPostsByProjectView.as_view(), name="post")
]
