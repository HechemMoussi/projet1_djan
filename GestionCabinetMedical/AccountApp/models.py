from django.db import models
from django.contrib.auth import AbstractUser
# Create your models here.
class User (AbstractUser):
    pass
class Doctor (User) :
    license_number=models.models.CharField(_(""), max_length=6, unique=True)
    phone=model.models.CharField(max_length=8,unique=True)



class Patient(User) :
    