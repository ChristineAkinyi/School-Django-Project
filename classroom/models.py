from django.db import models

# Create your models here.
# from django.db import models
# from teacher.models import Teacher

class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    # teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='classes')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    school_year = models.IntegerField()
    capacity = models.IntegerField()
    room_number = models.IntegerField()
    specialty = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

