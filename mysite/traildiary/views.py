from rest_framework import viewsets
from rest_framework import permissions
from .models import Region, Trail
from .serializers import RegionSerializer, TrailSerializer


class RegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows regions to be viewed or edited.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TrailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trails to be viewed or edited.
    """
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]