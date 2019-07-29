from django.db import models
import os


def get_image_path(instance, filename):
    """returns the path of the image"""
    return os.path.join('photos', str(instance.id), filename)

# Create your models here.
class Projects(models.Model):
    # Project Title
    title = models.CharField(max_length=255, null=False)
    # Projects short description
    shortDescription = models.CharField(max_length=255, null=False)
    # Projects Description
    description = models.TextField()
    # Projects Logo
    logo = models.ImageField(upload_to=get_image_path, blank=True, null=False)
    # Projects background image
    backgroundImage = models.ImageField(upload_to=get_image_path, blank=True, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.shortDescription)
