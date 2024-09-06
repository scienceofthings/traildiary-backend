from rest_framework import viewsets
from rest_framework import permissions

from django.conf import settings
from .models import Region, Trail
from .serializers import RegionSerializer, TrailDetailSerializer, TrailListSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CookieTokenObtainPairView(TokenObtainPairView):
    """
    Takes a set of user credentials, sets an access token as httpOnly cookie and the
    expiration date as non-httponly cookie.
    """

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        access_token = response.data["access"]
        """
        httponly: not accessible from JavaScript
        samesite: only accessible from the same domain
        max_age: as long as the access token lives (approximately)
        """
        response.set_cookie("access_token",
                            access_token,
                            httponly=True,
                            samesite='strict')
        response.set_cookie("user_is_authenticated",
                            settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                            httponly=False,
                            samesite='strict',
                            max_age=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'])


        # Unset refresh token in response because its already in the cookie
        response.data.pop("refresh", None)
        response.data.pop("access", None)

        return response


class RegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows regions to be viewed or edited.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TrailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trails to be viewed or edited.
    """
    queryset = Trail.objects.all()
    serializer_class = TrailListSerializer
    detail_serializer_class = TrailDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class

        return super(TrailViewSet, self).get_serializer_class()
