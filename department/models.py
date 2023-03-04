from django.db import models
from account.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Department(models.Model):
    dept=models.CharField(max_length=50,unique=True)
    deptid= models.IntegerField(unique=True)

    def __str__(self):
        return str(self.deptid)+"."+self.dept
class Subject(models.Model):
    subject=models.CharField(max_length=50,unique=True)
    sub_id=models.IntegerField(unique=True)
    def __str__(self):
        return str(self.sub_id)+"."+self.subject
class Branch(models.Model):
    branch=models.CharField(max_length=100)
    brachcode=models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.branch
class Lecture(models.Model):
    year=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(4)])
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    section = models.IntegerField(null=True)
    day = models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    faculty=models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)


    def __str__(self):
        return self.branch+',' + self.day +','+self.time
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return str(self.user) +"'s Profile"