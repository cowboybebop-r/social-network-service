from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from .serializers import PostSerializer
from .models import Post


class PostRetrieveListView(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        return super(PostRetrieveListView, self).list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super(PostRetrieveListView, self).retrieve(request, *args, **kwargs)
