from django.db.models.signals import post_save
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


def create_customer(sender, instance, created, **kwargs):
    if created:
        groupQuerySet = Group.objects.filter(name='customer')
        if (groupQuerySet.exists()):
            group = groupQuerySet.first()
        else:
            group = Group()
            group.name = 'customer'
            group.save()

        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username
        )
        print('account created!')


post_save.connect(create_customer, sender=User)
