from rest_framework import serializers

from .models import RequestLog


class RequestLogSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField('user.last_login', read_only=True)

    class Meta:
        model = RequestLog
        fields = ('id', 'user', 'last_request', 'last_login')
