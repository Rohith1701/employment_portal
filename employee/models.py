from django.db import models


GENDER_MALE = 'male'
GENDER_FEMALE = 'female'
GENDER_CHOICES =(
    (GENDER_MALE ,'male'),
    (GENDER_FEMALE, 'female'),
)

STATUS_PENDING ='pending'
STATUS_ACCEPTED ='accepted'
STATUS_REJECTED ='rejected'
STATUS_CHOICES =(
    (STATUS_PENDING ,'pending'),
    (STATUS_ACCEPTED ,'accepted'),
    (STATUS_REJECTED ,'rejected'),
)

class Employee(models.Model):

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=200 ,choices= GENDER_CHOICES , default=GENDER_MALE)
    mobile = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    expected_salery = models.IntegerField()
    will_relocate = models.BooleanField(default=False)



    def __str__(self):
        return self.name
     
class EmployeeJobMap(models.Model):
    Employee = models.ForeignKey(Employee ,on_delete=models.CASCADE)
    job = models.ForeignKey('jobs.job', on_delete=models.CASCADE)
    status = models.CharField(max_length=20 ,choices=STATUS_CHOICES ,default=STATUS_PENDING)
    feedback = models.TextField(blank=True,null= True)


    def __str__(self):
        return " {} - {} ".format(self.employee.name, self.job.position_name)
    
    # @property
    # def job_id(self):
    #     return self.job.id
    