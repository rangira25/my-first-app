from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class profile(models.Model):
    user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True,blank=True)
    last_name = models.CharField(max_length=200, null=True,blank=True)
    phone= models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return str(self.user)
   
def create_profile(sender,instance,create,**kwargs):
    if create:
        profile.objects.create(user=instance)
        print('user created')
post_save.connect(create_profile, sender=User)   

def update_profile(sender,instance,create,**kwargs):
    if create==False:
        instance.profile.save()
        print('user updated')
post_save.connect(create_profile, sender = User)