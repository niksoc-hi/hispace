from typing import Optional

from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from vote.models import UP, DOWN

from hispace.votes import VoteType


class VoteSerializer(serializers.Serializer):
    vote = serializers.SerializerMethodField()

    def get_vote(self, instance) -> Optional[VoteType]:
        user_id = self.context["request"].user.pk
        vote = instance.votes.get(user_id)
        if vote:
            return VoteType.UP if vote.action == UP else VoteType.DOWN
        return None


class VoteViewMixin:
    def get_queryset(self):
        queryset = super().get_queryset()

        user_id = self.request.user.pk
        return self.model.votes.annotate(queryset, user_id=user_id)

    @action(detail=True)
    def upvote(self, request, *args, **kwargs):
        instance = self.get_object()
        user_id = request.user.pk
        if not instance.votes.exists(user_id, UP):
            instance.votes.up(user_id)
        else:
            instance.votes.delete(user_id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=True)
    def downvote(self, request, *args, **kwargs):
        instance = self.get_object()
        user_id = request.user.pk
        if not instance.votes.exists(user_id, DOWN):
            instance.votes.down(user_id)
        else:
            instance.votes.delete(user_id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
