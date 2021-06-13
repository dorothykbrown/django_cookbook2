from django.contrib import admin
from .models import Recipe, Ingredient, Measurement, IngredientMeasurement

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Measurement)
admin.site.register(IngredientMeasurement)
