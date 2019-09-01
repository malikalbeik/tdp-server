from django.contrib import admin
from .models import Post, Image

# Register your models here.


class ImagesInLine(admin.TabularInline):
    model = Image
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
 
    list_display = ("title", "summary", "date_created", "is_published")
 
    inlines = [
        ImagesInLine
    ]
