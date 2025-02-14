from django.db import models

# Create your models here.
class Tracks(models.Model):
    title = models.CharField(max_length=50)
    title_kor = models.CharField(max_length=50)
    title_jap = models.CharField(max_length=50)
    featuring = models.TextField()

    def __str__(self):
        return self.title