from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework.routers import SimpleRouter

from contents import views as cv
from blog import views as bv
from project import views as pv


class OptionalSlashRouter(SimpleRouter):
    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()

router.register(r'contents', cv.ContentViewSet)
router.register(r'posts', bv.PostViewSet)
router.register(r'projects', pv.ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path('api/', include('project.urls')),
    # re_path('api/', include('blog.urls')), 
    re_path('api/', include(router.urls)),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls'))
]

admin.site.site_header = 'TDP Backend'
admin.site.site_title = 'TDP site Admin'
