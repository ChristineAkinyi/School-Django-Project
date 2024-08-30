from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    education_level = models.CharField(max_length=100)
    subject_specialization = models.CharField(max_length=100)
    bank_account_number = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField()
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"