# Generated by Django 4.2.15 on 2024-08-24 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_remove_teacher_education_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='education_level',
            field=models.CharField(default='Diploma', max_length=100),
            preserve_default=False,
        ),
    ]
