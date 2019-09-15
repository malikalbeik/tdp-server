from django.db import models
import os
import uuid
from project.models import Projects
from ckeditor.fields import RichTextField
from django_extensions.db.fields import AutoSlugField
from unidecode import unidecode
from field_permissions.models import FieldPermissionModelMixin


class PostManager(models.Manager):
    def get_queryset(self):
        return super(PostManager, self).get_queryset().filter(is_published=True)

def get_image_path(instance, filename):
    """returns the path of the image"""
    filename, file_extension = os.path.splitext(filename)
    return os.path.join('tdpServer', 'static', 'posts', str(uuid.uuid4()) + file_extension)


def slugify(content):
    content = unidecode(content)
    content = content.replace('_', '-').lower()
    return content.replace(" ", "-")

    
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', slugify_function=slugify)
    coverImage = models.ImageField(
        upload_to=get_image_path, blank=True, null=False)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    summary = models.TextField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    is_published = models.BooleanField(default=False)
    date_published = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()
    visible = PostManager()

    def __str__(self):
        return self.title if self.is_published else "[DRAFT] " + self.title

    class Meta:
        ordering = ['-is_published', '-date_published', '-date_created', ]
        permissions = [("can_change_post_is_published", "Can publish post"),]


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_path, verbose_name='Image')
