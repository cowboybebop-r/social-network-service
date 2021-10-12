from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from changelog.models import RequestLog
from changelog.serializers import RequestLogSerializer


class RequestLogView(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = RequestLog.objects.all()
    serializer_class = RequestLogSerializer

    def list(self, request, *args, **kwargs):
        return super(RequestLogView, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(RequestLogView, self).retrieve(request, *args, **kwargs)
