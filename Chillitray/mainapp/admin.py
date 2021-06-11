from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['tid','task_title','create_time_stamp']
    list_filter = ['create_time_stamp','tid']
    search_fields = ['task_title','task_description']
    