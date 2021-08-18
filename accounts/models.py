from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class MyAccountManage(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, gender, dob, middle_name=None, password=None):
        if not email:
            raise ValueError("User need email to continue")
        if not username:
            raise  ValueError("User must have a username")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            username=username,
            gender=gender,
            dob=dob,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, gender, dob, password, middle_name=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            username=username,
            gender=gender,
            dob=dob,
            password=password
        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superuser=True


class Account(AbstractBaseUser):
    GENDER = (("0", "Male"), ("1", "Female"), ("2", "Others"))
    first_name = models.CharField(max_length=30, )
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=GENDER, max_length=1)
    dob = models.DateField()

    signed_date = models.DateField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ('first_name', 'middle_name', 'lastname', 'username', 'email', 'gender', 'dob')
    objects = MyAccountManage()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True