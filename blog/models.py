from django.db import models
import os
import uuid
from ckeditor.fields import RichTextField


def get_image_path(instance, filename):
    """returns the path of the image"""
    filename, file_extension = os.path.splitext(filename)
    return os.path.join('static', 'posts', str(uuid.uuid4()) + file_extension)


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    coverImage = models.ImageField(
        upload_to=get_image_path, blank=True, null=False)
    summary = models.TextField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    content = RichTextField()

    is_published = models.BooleanField(default=False)
    date_published = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title if self.is_published else "[DRAFT] " + self.title

    class Meta:
        ordering = ['-is_published', '-date_published', '-date_created', ]


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_path, verbose_name='Image')