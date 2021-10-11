from rest_framework import serializers

from .models import Post, PostRate


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostRate
        fields = '__all__'
