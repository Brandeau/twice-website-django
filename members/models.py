from django.db import models

# Create your models here.


class Countries(models.Model):
    name = models.TextField(max_length=50)


class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    first_name_jap = models.CharField(max_length=30)
    last_name_jap = models.CharField(max_length=30)
    first_name_kor = models.CharField(max_length=30)
    last_name_kor = models.CharField(max_length=30)
    first_name_ch = models.CharField(max_length=30)
    last_name_ch = models.CharField(max_length=30)
    date_of_birth = models.IntegerField()
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name