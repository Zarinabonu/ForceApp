from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class Quater(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField()
    finish_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)