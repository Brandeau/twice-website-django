from django.contrib import admin
from .models import ReleaseGroup, Release, ReleaseFormat, ReleaseGroupType

# Register your models here.
class ReleaseGroupAdmin(admin.ModelAdmin):
    model = ReleaseGroup
    list_display = ['name', 'grouping', 'type']

admin.site.register(ReleaseGroup, ReleaseGroupAdmin)

class ReleaseAdmin(admin.ModelAdmin):
    model = Release
    list_display = ['title', 'release_year', 'format', 'country', 'release_group', 'annotation']
  

admin.site.register(Release, ReleaseAdmin)