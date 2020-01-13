from django.db import models

from app.model.class_ import Class
from app.model.teacher import Teacher


class Notification(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    notification = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)


class Notifications(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    notification = models.ForeignKey(Notification, on_delete=models.SET_NULL, null=True)