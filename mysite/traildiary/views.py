from rest_framework import viewsets
from rest_framework import permissions
from .models import Region, Trail
from .serializers import RegionSerializer, TrailDetailSerializer, TrailListSerializer


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