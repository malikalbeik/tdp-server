from django.contrib import admin
from .models import Projects

admin.site.register(Projects)

class ProjectAdmin(admin.ModelAdmin):
        list_display = ("title")
