
from django.urls import path
from .views import PostViewSet, ListProjectPostsView


urlpatterns = [
    path('posts/', PostViewSet.as_view({'get': 'list'}), name="posts-all"),
    path('posts/<slug:postSlug>/',
        ListProjectPostsView.as_view(), name="posts")
]