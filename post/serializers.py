from rest_framework import serializers

from .models import Post, PostRate


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'content', 'create_at', 'update_at')

    def create(self, validated_data):
        instance = self.Meta.model.objects.create(**validated_data)
        return instance


class PostRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostRate
        fields = '__all__'
