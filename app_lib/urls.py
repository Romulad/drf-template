from django.conf import settings

from rest_framework.request import Request
from urllib.parse import urlparse


def get_app_base_url(request: Request) -> str:
    """
    Get the base URL of the app.
    """
    url = urlparse(request.build_absolute_uri())
    return f"{url.scheme}://{url.hostname}"


def get_client_reset_password_url(
    request:Request,
    uuid: str, 
    token: str
) -> str:
    """
    Get client reset password URL.
    """
    origin = request.META.get('HTTP_ORIGIN', settings.CLIENT_BASE_URL)

    if not origin:
        return f"{get_app_base_url(request)}/auth/reset-password/{uuid}/{token}/"

    return f"{origin}/reset-password/{uuid}/{token}/"