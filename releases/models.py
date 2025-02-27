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
    grouping = models.ForeignKey(Grouping, on_delete=models.CASCADE, null=True, related_name="grouping_of_release_group")
    type = models.ForeignKey(ReleaseGroupType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
class Release(models.Model):
    title = models.CharField(max_length=50)
    release_year = models.IntegerField()
    format = models.ForeignKey(ReleaseFormat, on_delete=models.SET_NULL, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    release_group = models.ForeignKey(ReleaseGroup, on_delete=models.CASCADE)
    annotation = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


