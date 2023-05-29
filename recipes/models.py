from django.db import models
from django.contrib.auth.models import User


class Recipes(models.Model):
    title = models.CharField(max_length=150)
    ingredients = models.CharField(max_length=200)
    recipe = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")


