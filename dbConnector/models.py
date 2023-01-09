from django.db import models
from datetime import datetime
from django.utils import timezone
from nanoid import generate
# Create your models here.

class Metric(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(default='')
    description = models.TextField(default='')
    category = models.TextField(default='')


class Prompt(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(default='')
    description = models.TextField(default='')
    category = models.TextField(default='')


class Rubric(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(default='')
    description = models.TextField(default='')
    category = models.TextField(default='')


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(default='')
    description = models.TextField(default='')


class MentorText(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(default='')
    description = models.TextField(default='')
    category = models.TextField(default='')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True)
    created_on =  models.DateTimeField(default=timezone.now())

