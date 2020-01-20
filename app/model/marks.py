from django.db import models

from app.model.class_ import ClassMember, ClassSubject
from app.model.subject import Subject


class Marks(models.Model):
    class_member = models.ForeignKey(ClassMember, on_delete=models.SET_NULL, null=True)
    class_subject = models.ForeignKey(ClassSubject, on_delete=models.SET_NULL, null=True)
    mark = models.IntegerField()
    is_finil = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
