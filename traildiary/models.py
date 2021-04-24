from django.db import models
from .services import TrailDirectoryService

class Region(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Trail(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    technique = models.TextField()
    todo = models.TextField(blank=True)
    gpx_file_name = models.CharField(max_length=255, blank=True)
    gpx_points = models.JSONField(blank=True, default=list)
    directory = models.CharField(max_length=255)
    start_position = models.JSONField(blank=True, default=list)
    images = models.JSONField(blank=True, default=list)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        trail_directory_service = TrailDirectoryService(self.directory)
        self.gpx_file_name = trail_directory_service.get_gpx_file_name()
        self.start_position = trail_directory_service.get_start_position()
        self.gpx_points = trail_directory_service.get_gpx_points()
        self.images = trail_directory_service.get_responsive_images()
        super().save(*args, **kwargs)
