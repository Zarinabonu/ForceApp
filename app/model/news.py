from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100, null=True, default=True)
    short_content = models.TextField(null=True, default=True)
    full_content = models.TextField(null=True, default=True)
    image = models.ImageField()
    views = models.IntegerField(null=True, default=True)
    created = models.DateTimeField(auto_now_add=True)