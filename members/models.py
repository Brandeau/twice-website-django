from django.db import models
from groupings.models import Grouping

# Create your models here.


class Country(models.Model):
    name = models.TextField(max_length=50)


class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    first_name_jap = models.CharField(max_length=30, null=True)
    last_name_jap = models.CharField(max_length=30, null=True)
    first_name_kor = models.CharField(max_length=30, null=True)
    last_name_kor = models.CharField(max_length=30, null=True)
    first_name_ch = models.CharField(max_length=30, null=True)
    last_name_ch = models.CharField(max_length=30, null=True)
    date_of_birth = models.CharField(max_length=10, null=True)
    country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
    groupings = models.ManyToManyField(Grouping, related_name="groupings")

    def __str__(self):
        return self.first_name