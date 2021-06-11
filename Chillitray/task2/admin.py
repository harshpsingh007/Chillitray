from django.contrib import admin
from .models import Task2Model
# Register your models here.
@admin.register(Task2Model)
class Task2ModelAdmin(admin.ModelAdmin):
    list_display=['parent_id','task_id','title']
    list_filter = ['parent_id']
    search_fields = ["title"]