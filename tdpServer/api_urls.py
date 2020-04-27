from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from blog import views as bv
from contents import views as cv
from project import views as pv


class OptionalSlashRouter(SimpleRouter):
    def __init__(self):
        self.trailing_slash = "/?"
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()

router.register(r"contents", cv.ContentViewSet)
router.register(r"posts", bv.PostViewSet)
router.register(r"projects", pv.ProjectViewSet)

urlpatterns = [
    url(r"^v1/", include(router.urls)),
]
