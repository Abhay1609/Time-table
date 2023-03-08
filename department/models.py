from django.db import models
from account.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField

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
    branchcode=models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.branch
class PersonManager(models.Manager):
    def get_by_natural_key(self, branch, section):
        return self.get(branch=branch, section=section)
class Class(models.Model):
    objects=PersonManager
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    section=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(3)])
    class_id=models.CharField(max_length=5,unique=True)
    def natural_key(self):
        return str(self.branch)+str(self.section)

    def __str__(self):
        return str(self.branch)+"-"+str(self.section)
class Period(models.Model):
    period_no=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(9)])
    timeslot=models.CharField(max_length=11)
    def __str__(self):
        return str(self.period_no)+'.'+self.timeslot
class Lecture(models.Model):
    lecture_type=[
        ('THEORY','THEORY'),
        ('LAB','LAB'),
        ('OTHERS','OTHERS')
    ]
    period=models.ForeignKey(Period,on_delete=models.CASCADE)
    cid=models.ForeignKey(Class,on_delete=models.CASCADE)
    day = models.CharField(max_length=100)
    faculty=models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    type=models.CharField(choices=lecture_type,null=True,blank=True,max_length=7)
    class Meta:
        ordering=["day","period"]
        unique_together = (("faculty","day","period"),("cid","period","day"))
    def __str__(self):
        return str(self.cid)+","+str(self.period)
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    subject=models.ManyToManyField(Subject)


    def __str__(self):
        return str(self.user) +"'s Profile"
class Time_Table_Creator(models.Model):
    teacher_id=models.CharField(max_length=5)
    subject_id=models.CharField(max_length=5)
    class_id=ArrayField(models.CharField(max_length=5))
    no_of_lectures=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(9)])