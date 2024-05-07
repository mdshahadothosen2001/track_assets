from os import environ

from django.core.validators import RegexValidator

import jwt
from rest_framework.authentication import get_authorization_header
from rest_framework.pagination import PageNumberPagination

from config.JWT_SETTINGS import JWT_SETTINGS

PHONE_REGEX = RegexValidator(
    regex=r"^01[13-9]\d{8}$",
    message="Phone number must be 11 digit & this format: '01*********'",
)


def tokenValidation(request):
    """
    It takes the token from the request header, decodes it, and returns the payload
    :param request: The request object that was sent to the view
    :return: The payload of the token.
    """
    token_header = get_authorization_header(request).decode("utf-8")
    token_header_split = token_header.split(" ")
    if token_header_split[0] == "Bearer":
        token = token_header_split[1]
        payload = jwt.decode(
            jwt=token, key=JWT_SETTINGS["SIGNING_KEY"], algorithms=["HS256"]
        )
        return payload
    else:
        return None


def password_length_check(password):
    if (
        int(environ.get("LOWER_BOUND"))
        <= len(password)
        <= int(environ.get("UPPER_BOUND"))
    ):
        return True
    else:
        return False


class CustomPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = "page_size"
