from django.core.files.storage import FileSystemStorage
import gpxpy
import gpxpy.gpx


class TrailDirectoryService:
    filesystem = None

    def __init__(self, directory):
        self.filesystem = FileSystemStorage('uploads/' + directory)

    def chunk(self, lst, n):
        return zip(*[iter(lst)]*n)

    def get_gpx_file_name(self):
        for file in self.filesystem.listdir('.')[1]:
            if file.endswith(".gpx"):
                return file

    def get_gpx_points(self):
        points = []
        gpx_file_name = self.get_gpx_file_name()
        gpx_file = self.filesystem.open(gpx_file_name, 'r')
        gpx = gpxpy.parse(gpx_file)
        gpx.simplify(20)
        first_segment = gpx.tracks[0].segments[0]
        for point in first_segment.points:
            new_point = (point.latitude, point.longitude)
            points.append(new_point)
        return points

    def get_start_position(self):
        first_point = self.get_gpx_points()[0]
        return first_point

    def get_responsive_images(self):
        responsive_images_chunked = []
        responsive_images = self.filesystem.listdir('./responsiveImages')[1]
        responsive_images.sort()
        for chunk in self.chunk(responsive_images, 3):
            responsive_images_chunked.append(chunk)
        return responsive_images_chunked
