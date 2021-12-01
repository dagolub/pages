from django.db import models


class Page(models.Model):
    url = models.CharField(max_length=200)
    html = models.TextField()
