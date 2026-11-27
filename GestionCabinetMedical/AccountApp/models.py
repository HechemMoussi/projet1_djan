from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError


class User(AbstractUser):
    pass


number_validator = RegexValidator(
    r'^\d{8}$',
    'Phone number must be exactly 8 digits.'
)


def birth_date_validator(date):
    if date >= timezone.localdate():
        raise ValidationError("Birth date must be in the past.")


class Specialty(models.Model):
    name = models.CharField(max_length=50)
    class Meta():
        verbose_name="specialty"
        verbose_name_plural="specialities"
        
    def __str__(self):
        return self.name


class Doctor(User):
    license_number = models.CharField(
        max_length=6, unique=True,
        validators=[MinLengthValidator(6), MaxLengthValidator(6)]
    )
    phone = models.CharField(max_length=8, unique=True, validators=[number_validator])
    specialties = models.ManyToManyField(Specialty, related_name='doctors')
    def __str__(self):
                return f"Dr. {self.first_name} {self.last_name}"
    class Meta():
            verbose_name="Doctor"
            verbose_name_plural="Doctors"
            


class Patient(User):
    national_id = models.CharField(max_length=8, unique=True, validators=[number_validator])
    phone = models.CharField(max_length=8, unique=True, validators=[number_validator])
    birth_date = models.DateField(blank=True, null=True, validators=[birth_date_validator])
    def __str__(self):
                    return f"P. {self.first_name} {self.last_name}"

    class Meta():
                verbose_name="Patient"
                verbose_name_plural="Patients"