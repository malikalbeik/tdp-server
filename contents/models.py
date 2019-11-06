from django.db import models
from ckeditor.fields import RichTextField
import uuid, os
from django_extensions.db.fields import AutoSlugField
from unidecode import unidecode

def get_image_path(instance, filename):
    """returns the path of the image"""
    filename, file_extension = os.path.splitext(filename)
    return os.path.join('tdpServer', 'static', 'posts', str(uuid.uuid4()) + file_extension)


def slugify(content):
    content = unidecode(content)
    content = content.replace('_', '-').lower()
    return content.replace(" ", "-")

class Content(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', slugify_function=slugify)
    content = RichTextField()
    image = models.ImageField(
        upload_to=get_image_path, blank=True, null=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']
