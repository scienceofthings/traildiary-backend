from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import HTTP_HEADER_ENCODING


class JWTAndCookieAuthentication(JWTAuthentication):
    """
    An authentication plugin that authenticates requests through a JSON web
    token provided in a cookie.
    """
    def authenticate(self, request):
        raw_token = bytes
        cookie = request.COOKIES.get("access_token")
        if cookie is None:
            return None

        if isinstance(cookie, str):
            raw_token = cookie.encode(HTTP_HEADER_ENCODING)

        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token
