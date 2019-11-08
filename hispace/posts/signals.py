from actstream.models import followers
from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify

from hispace import comments
from .models import Post


@receiver(post_save, sender=Post)
def on_post_create(sender, instance, created, **kwargs):
    post = instance
    if created:
        notify.send(
            post.user,
            recipient=followers(post.user),
            verb="created a post",
            action_object=post,
        )


@receiver(post_save, sender=comments.get_model())
def on_comment_create(sender, instance, created, **kwargs):
    comment = instance
    if created:
        notify.send(
            comment.user,
            recipient=followers(comment.post),
            verb="wrote a comment",
            action_object=comment,
            target=comment.post,
        )
        notify.send(
            comment.user,
            recipient=followers(comment.user),
            verb="wrote a comment",
            action_object=comment,
        )
