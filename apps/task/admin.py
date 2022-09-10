from django.contrib import admin
from .models import task, project, routine,  week
# Register your models here.
admin.site.register(task)
admin.site.register(project)
admin.site.register(routine)
admin.site.register(week)