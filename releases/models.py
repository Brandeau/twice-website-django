from django.db import models
from groupings.models import Groupings
from members.models import Countries

# Create your models here.

class ReleaseFormats(models.Model):
    format = models.CharField(max_length=50)

    def __str__(self):
        return self.format
    
class ReleaseGroupType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type
    
class ReleaseGroups(models.Model):
    name = models.CharField(max_length=50)
    grouping_id = models.ForeignKey(Groupings, on_delete=models.CASCADE, related_name="releases")
    type_id = models.ForeignKey(ReleaseGroupType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
class Releases(models.Model):
    title = models.CharField(max_length=50)
    release_year = models.IntegerField()
    format_id = models.ForeignKey(ReleaseFormats, on_delete=models.SET_NULL, null=True)
    country_id = models.ForeignKey(Countries, on_delete=models.SET_NULL, null=True)
    release_group_id = models.ForeignKey(ReleaseGroups, on_delete=models.CASCADE)
    annotation = models.TextField(max_length=200)

    def __str__(self):
        return self.title

class Tracks(models.Model):
    title = models.CharField(max_length=50, null=False)
    title_kor = models.CharField(max_length=50)
    title_jap = models.CharField(max_length=50)
    featuring = models.CharField(max_length=50)
    releases = models.ManyToManyField(Releases)
