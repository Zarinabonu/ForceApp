from django.db import models

from app.model.class_ import ClassSubject
from app.model.student import Student


class Attandance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    class_subject = models.ForeignKey(ClassSubject, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    attandance = models.BooleanField(default=False)