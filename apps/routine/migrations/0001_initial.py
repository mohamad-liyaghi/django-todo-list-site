# Generated by Django 4.0.4 on 2022-09-11 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('detail', models.TextField()),
                ('token', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('time', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
                ('repeat', models.CharField(choices=[('o', 'Once'), ('d', 'Daily'), ('m', 'Mon To Fri')], default='o', max_length=1)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
