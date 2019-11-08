from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel
from vote.models import VoteModel

from hispace.tags.models import TaggableModel


class Post(TimeStampedModel, TaggableModel, VoteModel, models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )

    def __str__(self):
        return f"{self.title} {self.user}"
