from django.db.models import fields
from ..models import Task2Model
from rest_framework import serializers

class Task2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Task2Model
        fields = ['task_id','title','parent_id']
