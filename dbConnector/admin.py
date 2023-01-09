from django.contrib import admin
from dbConnector.models import *
model_list = [Rubric, Skill, Prompt, MentorText, Metric]
admin.site.register(model_list)