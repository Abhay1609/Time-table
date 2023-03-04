
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.validators import MinValueValidator, MaxValueValidator
from department.models import Department,Subject




class UserManager(BaseUserManager):
    def create_user(self,email,department, full_name ,age, gender,mobile_number, password=None):
        """
        Creates and saves a User with the given email, name ,tc and password.
        """
        if not mobile_number:
            raise ValueError('Users must have a Mobile Number.')
        if not email:
            raise ValueError('Users must have a Email.')

        user = self.model(
            mobile_number=mobile_number,
            email=self.normalize_email(email),
            department=department,
            full_name=full_name,
            gender=gender,
            age=age,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email, full_name  ,department,age, gender,mobile_number,password=None):
        """
        Creates and saves a superuser with the given email, name , tc and password.
        """
        if not mobile_number:
            raise ValueError('Users must have a Mobile number.')
        if not email:
            raise ValueError('Users must have a Email.')
        user = self.create_user(
            mobile_number=mobile_number,
            password=password,
            email=email,
            full_name=full_name,
            department=department,
            gender=gender,
            age=age,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    full_name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    mobile_number=models.CharField(max_length=10,unique=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    subject=models.ManyToManyField(Subject)
    gender=models.CharField(max_length=10,null=True)
    age=models.IntegerField(validators=[MinValueValidator(18),MaxValueValidator(60)])
    isverified=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)



    objects=UserManager()


    USERNAME_FIELD='mobile_number'
    REQUIRED_FIELDS= ['email','full_name','age','gender','department']

    def __str__(self):
        return self.full_name+  ' , ' +self.mobile_number

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    def cookies(self):
        refresh=RefreshToken.for_user(self)
        return{
            'refresh': str(refresh),
            'access':str(refresh.access_token)
        }

class lecture(models.Model):
    year=models.IntegerField()
    branche=models.CharField(max_length=100)
    section = models.IntegerField()
    day = models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    faculty=models.CharField(max_length=100)
    subject = models.CharField(max_length=100)


    def __str__(self):
        return self.branche+','+ self.year + ',' + self.section + ',' + self.day +','+self.time






# Create your models here.