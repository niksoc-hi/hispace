from rest_framework import serializers

from hispace.users.api.serializers import UserSerializer
from hispace.votes.api.mixins import VoteSerializer
from .. import get_model


class CommentSerializer(VoteSerializer, serializers.ModelSerializer):
    vote = serializers.SerializerMethodField()
    user = UserSerializer()

    class Meta:
        model = get_model()
        fields = "user", "comment", "submit_date", "vote"
        read_only_fields = "user", "post", "vote"
