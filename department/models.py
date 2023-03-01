from django.db import models


# Create your models here.

class department(models.Model):
    deptid= models.IntegerField(max_length=3,unique=True)