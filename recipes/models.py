from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingrendients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.name