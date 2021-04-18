from django.core.files.storage import FileSystemStorage
import gpxpy
import gpxpy.gpx
from os import path
from django.conf import settings


class TrailDirectoryService:
    filesystem = None
    directory = ''
    gpx_file_name_without_path = ''

    def __init__(self, directory):
        self.directory = directory
        self.filesystem = FileSystemStorage(
            path.join(settings.MEDIA_ROOT, settings.DIARY_FILES_SUBDIRECTORY, self.directory)
        )

    def chunk(self, lst, n):
        return zip(*[iter(lst)]*n)

    def get_gpx_file_name(self):
        filename = self._get_gpx_file_name_without_path()
        return self._get_relative_path_to_document_root(filename)

    def _get_gpx_file_name_without_path(self):
        if self.gpx_file_name_without_path != '':
            return self.gpx_file_name_without_path
        for file in self.filesystem.listdir('.')[1]:
            if file.endswith(".gpx"):
                self.gpx_file_name_without_path = file
                return self.gpx_file_name_without_path

    def get_gpx_points(self):
        points = []
        gpx_file_name = self._get_gpx_file_name_without_path()
        gpx_file = self.filesystem.open(gpx_file_name, 'r')
        gpx = gpxpy.parse(gpx_file)
        gpx.simplify(5)
        first_segment = gpx.tracks[0].segments[0]
        for point in first_segment.points:
            new_point = (point.latitude, point.longitude)
            points.append(new_point)
        return points

    def _get_relative_path_to_document_root(self, filename):
        return path.join(settings.DIARY_FILES_SUBDIRECTORY, self.directory, filename)

    def get_start_position(self):
        first_point = self.get_gpx_points()[0]
        return first_point

    def get_responsive_images(self):
        responsive_images_chunked = []
        responsive_images_with_path = []
        responsive_images = self.filesystem.listdir('./')[1]
        for responsive_image in responsive_images:
            responsive_images_with_path.append(self._get_relative_path_to_document_root(responsive_image))
        responsive_images_with_path.sort()
        for chunk in self.chunk(responsive_images_with_path, 3):
            responsive_images_chunked.append(chunk)
        return responsive_images_chunked
