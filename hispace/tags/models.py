from django.db import models
from taggit.managers import TaggableManager


class TaggableModel(models.Model):
    tags = TaggableManager()

    class Meta:
        abstract = True
