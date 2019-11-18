from rest_framework import serializers


class TagsSerializer(serializers.Serializer):
    """must be inherited from before serializers.ModelSerializer"""

    tags = serializers.StringRelatedField(many=True, allow_empty=False)

    def create(self, validated_data):
        tags = validated_data.pop("tags")
        instance = super().create(validated_data)
        instance.tags.add(*tags["names"])
        return instance

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags")
        modified_instance = super().update(instance, validated_data)
        modified_instance.tags.clear()
        modified_instance.tags.add(*tags["names"])
        return modified_instance
