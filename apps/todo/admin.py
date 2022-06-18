from django.contrib import admin
from .models import task, project
# Register your models here.
admin.site.register(task)
admin.site.register(project)