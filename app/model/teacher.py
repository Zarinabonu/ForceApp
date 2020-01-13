from django.db import models

from app.model.account import Account


class Teacher(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)