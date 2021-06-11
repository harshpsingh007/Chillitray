from django.db import models
from django.db.models.fields import AutoField, CharField, DateTimeField, TextField
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    tid = AutoField(primary_key=True)
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    task_title = CharField(max_length=200)
    task_description = TextField(max_length=2000,null=True,blank=True)
    task_pic = models.ImageField(upload_to="media/task_pics")
    create_time_stamp = DateTimeField(auto_created=True,auto_now_add=True)

    class Meta:
        ordering=['tid']