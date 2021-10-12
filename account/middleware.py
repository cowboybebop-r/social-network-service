from django.utils.timezone import now
from rest_framework_simplejwt import authentication

from account.models import User


class LastRequestMiddleware(object):
    """
    Middle ware which handle all requests and save in model.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            # Getting JWT token from the requests and loading request.user to the user associated to that model
            request.user = authentication.JWTAuthentication().authenticate(request)[0]
        except Exception as ex:
            print(ex)

        if not request.user.is_anonymous:
            User.objects.filter(pk=request.user.pk).update(last_request=now())
