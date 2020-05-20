from django.db import models
from users.models import CustomUser

# Create your models here.

class ClassRoom(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)


class Subjects(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    schedule = models.CharField(max_length=100, null=False, default="NO HORARIO")
    fk_idclassroom = models.ForeignKey(ClassRoom, on_delete=models.DO_NOTHING)
    fk_idteacher = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)



class Grades(models.Model):
    fk_iduser = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    fk_idsubject = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING)
    first_trimester = models.FloatField(default=0)
    second_trimester = models.FloatField(default=0)
    third_trimester = models.FloatField(default=0)
    final_exam = models.FloatField(default=0)
    average = models.FloatField(default=0)