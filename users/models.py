from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=128, null=False)
    last_name = models.CharField(max_length=128, null=False)
    role = models.CharField(max_length=50, default=0)
    fk_idclassroom = models.ForeignKey('classroom.ClassRoom', on_delete=models.DO_NOTHING, null=True)
    

    def __str__(self):
        return self.email
        #return str(self.id)


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print("/"*50)
        print("USER CREATED")
        print("/"*50)