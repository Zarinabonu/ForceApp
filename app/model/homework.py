from django.db import models

from app.model import Subject, ClassSubject


class Homework(models.Model):
    class_subject = models.ForeignKey(ClassSubject, on_delete=models.SET_NULL, null=True)
    name = models.TextField(null=True, blank=True)