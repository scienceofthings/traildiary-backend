from .models import Region, Trail
from rest_framework import serializers


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'title']


class TrailListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = ['id', 'title', 'region', 'start_position']


class TrailDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = ['id', 'title', 'description', 'technique', 'todo', 'region', 'gpx_file_name',
                  'gpx_points', 'start_position', 'images']