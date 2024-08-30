from django.db import models
from course.models import Course

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    student_id = models.AutoField(primary_key=True)
    student_code = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    bio = models.TextField()
    courses = models.ManyToManyField(Course)
    guardian_name = models.CharField(max_length=40)
    guardian_phone_number = models.CharField(max_length=20)
    picture = models.ImageField()

def __str__(self):
    return f"{self.first_name} {self.last_name}"