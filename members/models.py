from django.db import models

# Create your models here.


class Countries(models.Model):
    name = models.TextField(max_length=50)


class Member(models.Model):
    first_name = models.TextField(max_length=30)
    last_name = models.TextField(max_length=30)
    first_name_jap = models.TextField(max_length=30)
    last_name_jap = models.TextField(max_length=30)
    first_name_kor = models.TextField(max_length=30)
    last_name_kor = models.TextField(max_length=30)
    first_name_ch = models.TextField(max_length=30)
    last_name_ch = models.TextField(max_length=30)
    date_of_birth = models.IntegerField()
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name