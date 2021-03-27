from .models import Region, Trail
from rest_framework import serializers


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'title']


class TrailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trail
        fields = ['id', 'title', 'description', 'technique', 'todo', 'directory', 'region', 'gpx_file_name',
                  'gpx_points', 'start_position']
