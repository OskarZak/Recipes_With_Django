from django.contrib import admin
from . import models

class RecipesAdmin(admin.ModelAdmin):
    list_display = ("title",)


admin.site.register(models.Recipes, RecipesAdmin )