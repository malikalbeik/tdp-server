from django.contrib import admin
from django.urls import path
from contents import views as cv
from blog import views as bv
from project import views as pv


admin.site.site_header = "TDP Backend"
admin.site.site_title = "Control Panel"
admin.sites.AdminSite.index_title = "Control Panel"

urlpatterns = [
    path("", admin.site.urls),
]
