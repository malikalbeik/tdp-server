from django.db import models
import os
import uuid


def get_image_path(instance, filename):
    """returns the path of the image"""
    filename, file_extension = os.path.splitext(filename)
    return os.path.join('tdpServer', 'static', 'projects', str(uuid.uuid4()) + file_extension)

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
    # Projects instagram account
    instagramAccount = models.CharField(max_length=50, blank=True)
    # Projects twitter account
    twitterAccount = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.shortDescription)
