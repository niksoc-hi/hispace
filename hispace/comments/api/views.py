from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from hispace.comments.api.serializers import CommentSerializer
from .. import get_model
from hispace.votes.api.mixins import VoteViewMixin


class CommentViewSet(VoteViewMixin, NestedViewSetMixin, ModelViewSet):
    model = get_model()
    queryset = get_model().objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs["parent_lookup_post_id"]
        serializer.save(post_id=post_id, user=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.user != self.request.user:
            raise PermissionDenied
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied
        instance.delete()
