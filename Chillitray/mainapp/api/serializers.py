from django.contrib.auth.models import User
from django.db.models import fields
from ..models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["tid","uid","task_title","task_description","task_pic","create_time_stamp"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","first_name","last_name","username"]