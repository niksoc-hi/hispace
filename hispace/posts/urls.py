from rest_framework_extensions.routers import ExtendedSimpleRouter

from .api.views import PostViewSet, PostCommentViewSet

app_name = "posts"

router = ExtendedSimpleRouter()

router.register(r"", PostViewSet, base_name="post").register(
    r"comments",
    PostCommentViewSet,
    basename="posts-comment",
    parents_query_lookups=["object_pk"],
)

urlpatterns = router.urls
