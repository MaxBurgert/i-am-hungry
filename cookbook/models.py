from django.db import models

from cookbook.choices import PREPARATION_TIME_CHOICES


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    recipe_ingredient = models.CharField(max_length=200)
    recipe_time = models.CharField(
        max_length=1, choices=PREPARATION_TIME_CHOICES, default="S"
    )
    recipe_source = models.CharField(max_length=200)

    def __str__(self):
        return self.recipe_name
