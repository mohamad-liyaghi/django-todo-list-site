# Generated by Django 4.0.4 on 2022-09-12 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_task_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='project',
        ),
    ]
