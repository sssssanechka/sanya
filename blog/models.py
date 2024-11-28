from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=255,
        )
    text = models.CharField(
        max_length=1000,
        )

