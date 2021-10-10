import json

from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # If `token` key will be received as part of the response, it will be a
        # byte object. Byte objects don't serialize well, so it needed to
        # decode before rendering the User object.

        token = data.get('token', None)

        if token is not None and isinstance(token, type(bytes)):
            data['token'] = token.decode('utf-8')

        return json.dumps({
            'user': data
        })
