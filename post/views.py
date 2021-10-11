from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .permissions import IsPostOwner
from .serializers import PostSerializer
from .models import Post, PostRate
from account.models import User


class PostRetrieveListView(GenericViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsPostOwner]

    def list(self, request, *args, **kwargs):
        return super(PostRetrieveListView, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PostRetrieveListView, self).retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data.copy()
        data['user'] = user.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['post'], detail=True)
    def like(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.pk)
        post = self.get_object()
        obj, created = PostRate.objects.get_or_create(liked_by=user, liked_post=post)
        if not created:
            obj.liked = True
            obj.save()
        data = {
            'total_likes': PostRate.objects.filter(liked=True, liked_post=post).count(),
            'total_dislikes': PostRate.objects.filter(liked=False, liked_post=post).count()
        }
        return JsonResponse(data)

    @action(methods=['post'], detail=True)
    def unlike(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.pk)
        post = self.get_object()
        obj, created = PostRate.objects.get_or_create(liked_by=user, liked_post=post)
        if not created:
            obj.liked = False
            obj.save()
        data = {
            'total_likes': PostRate.objects.filter(liked=True, liked_post=post).count(),
            'total_dislikes': PostRate.objects.filter(liked=False, liked_post=post).count()
        }
        return JsonResponse(data)
