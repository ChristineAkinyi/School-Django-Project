# Generated by Django 4.2.15 on 2024-08-24 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='teacher',
        ),
    ]
