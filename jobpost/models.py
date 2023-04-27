from django.db import models
from django.contrib.auth.models import User


class JobPost(models.Model):

    jobname = models.CharField(max_length=200)
    companyname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    salery = models.IntegerField()

    def __str__(self):
        return self.jobname
 