from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from .permissions import IsPostOwner
from .serializers import PostSerializer
from .models import Post


class PostRetrieveListView(GenericViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, IsPostOwner]

    def list(self, request, *args, **kwargs):
        return super(PostRetrieveListView, self).list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super(PostRetrieveListView, self).retrieve(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super(PostRetrieveListView, self).create(request, *args, **kwargs)
