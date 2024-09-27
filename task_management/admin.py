from django.contrib import admin
from . models import Category, Subtask,Task
# Register your models here.

admin.site.register(Task)
admin.site.register(Subtask)
admin.site.register(Category)