from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    recipe_ingredient = models.CharField(max_length=200)
    recipe_source = models.CharField(max_length=200)
