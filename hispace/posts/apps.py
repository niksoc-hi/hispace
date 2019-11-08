from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = "hispace.posts"

    def ready(self):
        # from follows.utils import register
        # from .signals import on_comment_create, on_post_create
        #
        # register("posts", self.get_model("Post"))
        pass
