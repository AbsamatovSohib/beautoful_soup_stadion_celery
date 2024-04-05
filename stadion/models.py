from django.db import models


class Club(models.Model):
    title = models.CharField(max_length=50)
    position = models.CharField(max_length=2)
    game = models.CharField(max_length=3)
    score = models.CharField(max_length=3)

