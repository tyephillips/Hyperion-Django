from django.contrib import admin
from .models import Question, Choice

# Registeering the Question and Choice model in the admin site.
# This allows you to manage questions and choices through 
# the admin interface.
admin.site.register(Question)
admin.site.register(Choice)
