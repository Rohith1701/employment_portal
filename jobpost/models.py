from django.db import models
from django.contrib.auth.models import User


class JobPost(models.Model):
    jobname = models.CharField(max_length=200, null=True)
    companyname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200,  null=True)
    mobile = models.CharField(max_length=10,  null=True)
    city = models.CharField(max_length=10,  null=True)
    salery = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.jobname

 
class InputForm1(models.Model):
 
    first_name1 = models.CharField(max_length = 200)
    last_name1 = models.CharField(max_length = 200)
    roll_number1 = models.IntegerField(help_text = "Enter 6 digit roll number")
    password1 = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name