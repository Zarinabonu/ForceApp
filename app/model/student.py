from django.db import models

from app.model.account import Account
from app.model.school import School


class Student(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)