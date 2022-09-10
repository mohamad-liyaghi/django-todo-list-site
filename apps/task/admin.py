from django.contrib import admin
from .models import Task, project, routine,  week
# Register your models here.
admin.site.register(Task)
admin.site.register(project)
admin.site.register(routine)
admin.site.register(week)