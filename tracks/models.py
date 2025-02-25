from django.db import models
from releases.models import Release

# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length=50, null=False)
    title_kor = models.CharField(max_length=50, null=True)
    title_jap = models.CharField(max_length=50, null=True)
    featuring = models.CharField(max_length=50, null=True)
    releases = models.ManyToManyField(Release, through="TrackNum", related_name="releases")

    def __str__(self):
        return self.title

class TrackNum(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    track_num = models.IntegerField()

    def __str__(self):
        return "{}_{}".format(self.release.__str__(), self.track.__str__())