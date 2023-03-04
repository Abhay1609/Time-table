from django.db import models

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

class Lecture(models.Model):
    year=models.IntegerField()
    branche=models.CharField(max_length=100)
    section = models.IntegerField()
    day = models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    faculty=models.CharField(max_length=100)
    subject = models.CharField(max_length=100)


    def __str__(self):
        return self.branche+','+ self.year + ',' + self.section + ',' + self.day +','+self.time



