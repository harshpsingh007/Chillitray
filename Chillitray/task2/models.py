from django.db import models
from django.db.models.fields import AutoField, CharField, SlugField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
# Create your models here.
class Task2Model(models.Model):
    parent_id = ForeignKey(User,on_delete=models.CASCADE)
    task_id = AutoField(primary_key=True)
    title = CharField(max_length=100,blank=False)

    class Meta:
        ordering=["task_id"]