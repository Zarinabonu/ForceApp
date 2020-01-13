from random import randint, randrange

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    f_name = models.CharField(max_length=100, null=True, blank=True)
    l_name = models.CharField(max_length=100, null=True, blank=True)
    m_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Account)
def create_user(sender, instance, created, **kwargs):
    if created:
        l = instance.l_name
        f = instance.f_name
        username = l+f
        value = randrange(100, 999)
        u = User.objects.create(username=username)
        u.set_password(value)
        u.save()
        instance.user = u
        instance.save()
