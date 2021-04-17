from django.contrib import admin

from .models import Region
from .models import Trail

class TrailAdmin(admin.ModelAdmin):
    exclude = ('startPositionLat','startPositionLng')

admin.site.register(Region)
admin.site.register(Trail, TrailAdmin)
