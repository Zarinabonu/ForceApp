from django.db import models

from app.model.student import Student
from app.model.subject import Subject, Quater
from app.model.teacher import Teacher


class Class(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True, default=True)
    created = models.DateTimeField(auto_now_add=True)


class ClassMember(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)


class ClassSubject(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    quater = models.ForeignKey(Quater, on_delete=models.SET_NULL, null=True)
    start_date = models.TimeField()
    finish_date = models.TimeField()
    day = models.DateField()




