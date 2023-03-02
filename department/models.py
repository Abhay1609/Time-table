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