from rest_framework import serializers

from hispace.tags.api.mixins import TagsSerializer
from hispace.users.api.serializers import UserSerializer
from hispace.votes.api.mixins import VoteSerializer
from ..models import Post


class PostSerializer(VoteSerializer, TagsSerializer, serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        fields = "__all__"
        model = Post
        read_only_fields = (
            "num_vote_up",
            "num_vote_down",
            "vote_score",
        )  # TODO how can we abstract the vote fields
