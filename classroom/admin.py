from django.contrib import admin
from classroom.models import ClassRoom, Subjects, Grades

# Register your models here.

admin.site.register(ClassRoom)
admin.site.register(Subjects)
admin.site.register(Grades)