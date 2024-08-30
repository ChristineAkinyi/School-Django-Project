from django.db import models
from classroom.models import Classroom
from teacher.models import Teacher

# Create your models here.

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    course_department = models.TextField(max_length=200)
    course_trainer = models.TextField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    course_status = models.CharField(max_length=30, default='active')
    max_number_of_students = models.PositiveIntegerField(default=35)
    course_level = models.CharField(max_length=30)
    trainer = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    classes = models.ManyToManyField(Classroom, related_name='classes')

    def __str__(self):
        return self.course_name
