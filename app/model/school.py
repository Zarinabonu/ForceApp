from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100, null=True, default=True)
    created = models.DateTimeField(auto_now_add=True)