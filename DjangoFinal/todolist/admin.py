from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'due_date', 'priority', 'completed')

admin.site.register(Task, TaskAdmin)