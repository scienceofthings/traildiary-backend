from django.contrib import admin

from .models import Region
from .models import Trail


class TrailAdmin(admin.ModelAdmin):
    exclude = ('gpx_file_name', 'gpx_points', 'start_position', 'images')


admin.site.register(Region)
admin.site.register(Trail, TrailAdmin)
