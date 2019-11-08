from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from comments.api.views import CommentViewSet
from ..models import Post
from votes.api.mixins import VoteViewMixin
from .serializers import PostSerializer


class PostViewSet(VoteViewMixin, NestedViewSetMixin, ModelViewSet):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["user"]
    search = ["tags__name"]

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get("search")
        if search_term:
            queryset = queryset.filter(
                Q(tags__name__in=[search_term]) | Q(tags__slug__in=[search_term])
            ) | queryset.filter(title__contains=search_term)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.user != self.request.user:
            raise PermissionDenied
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied
        instance.delete()


class PostCommentViewSet(CommentViewSet):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(content_type=ContentType.objects.get_for_model(Post))
        )
