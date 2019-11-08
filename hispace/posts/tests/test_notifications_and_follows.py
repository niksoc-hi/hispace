from unittest import mock

from django.test import TestCase
from notifications import views
from notifications.models import Notification

from follows.views import follow
from heavy.models import User
from posts.models import Post, Comment


# TODO: figure out a way to test this in notifications and follows app/package
# problem is that we need a model to follow
class TestNotificationsAndFollows(TestCase):
    def test_start(self):
        user1 = User.objects.create_user("1")
        post_follower = User.objects.create_user("2")
        user1_follower = User.objects.create_user("3")
        post = Post.objects.create(user=user1, title="title")

        request = mock.Mock()
        request.user = post_follower
        request.GET = {}
        request.POST = {}
        follow(request, "posts", post.id)

        request = mock.Mock()
        request.user = user1_follower
        request.GET = {}
        request.POST = {}
        follow(request, "users", user1.id)

        Comment.objects.create(user=user1, post=post, description="description")
        request.method = "GET"
        a = views.UnreadNotificationsList.as_view()(request)
