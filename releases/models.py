from django.db import models
from groupings.models import Grouping
from members.models import Country

# Create your models here.

class ReleaseFormat(models.Model):
    format = models.CharField(max_length=50)

    def __str__(self):
        return self.format
    
class ReleaseGroupType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type
    
class ReleaseGroup(models.Model):
    name = models.CharField(max_length=50)
    grouping_id = models.ForeignKey(Grouping, on_delete=models.CASCADE, related_name="releases")
    type_id = models.ForeignKey(ReleaseGroupType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
class Release(models.Model):
    title = models.CharField(max_length=50)
    release_year = models.IntegerField()
    format_id = models.ForeignKey(ReleaseFormat, on_delete=models.SET_NULL, null=True)
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    release_group_id = models.ForeignKey(ReleaseGroup, on_delete=models.CASCADE)
    annotation = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.title


