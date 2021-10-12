from collections import Counter
from itertools import groupby

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import action, permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from django_filters import rest_framework as filters

from .filters import DateRangeFilterSet
from .permissions import IsPostOwner
from .serializers import PostSerializer
from .models import Post, PostRate
from account.models import User


class PostCreateRetrieveListView(GenericViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @permission_classes([IsAuthenticatedOrReadOnly])
    def list(self, request, *args, **kwargs):
        return super(PostCreateRetrieveListView, self).list(request, *args, **kwargs)

    @permission_classes([IsAuthenticatedOrReadOnly])
    def retrieve(self, request, *args, **kwargs):
        return super(PostCreateRetrieveListView, self).retrieve(request, *args, **kwargs)

    @permission_classes([IsPostOwner])
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
    @permission_classes([IsAuthenticated])
    def like(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.pk)
        post = self.get_object()
        obj, created = PostRate.objects.get_or_create(liked_by=user, liked_post=post)
        obj.liked = True
        obj.save()
        data = {
            'total_likes': PostRate.objects.filter(liked=True, liked_post=post).count(),
            'total_dislikes': PostRate.objects.filter(liked=False, liked_post=post).count()
        }
        return JsonResponse(data)

    @action(methods=['post'], detail=True)
    @permission_classes([IsAuthenticated])
    def dislike(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.pk)
        post = self.get_object()
        obj, created = PostRate.objects.get_or_create(liked_by=user, liked_post=post)
        obj.liked = False
        obj.save()
        data = {
            'total_likes': PostRate.objects.filter(liked=True, liked_post=post).count(),
            'total_dislikes': PostRate.objects.filter(liked=False, liked_post=post).count()
        }
        return JsonResponse(data)


class AnalyticView(GenericAPIView):
    queryset = PostRate.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DateRangeFilterSet

    def get(self, request, format=None):
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)

        ordered_queryset = filtered_queryset.order_by('create_at')
        likes_by_date = groupby(ordered_queryset,
                                lambda like: like.create_at.strftime("%Y-%m-%d"))

        analytics = []
        for date, likes in likes_by_date:
            count = Counter(like.liked for like in likes)
            analytics.append(
                {
                    'date': date,
                    'total_likes': count.get(True),
                }
            )
        if len(analytics) == 0:
            analytics.append(
                {
                    'message': 'No likes in this interval'
                }
            )

        return Response(analytics)
