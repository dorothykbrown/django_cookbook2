from django.db import models

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=250)
    instructions = models.TextField()
    image = models.ImageField(upload_to='cookbook/images')
    author = models.CharField(max_length=250)
    public = models.BooleanField(default=False)
    category = models.CharField(max_length=250)
    difficulty = models.CharField(max_length=250)
    ingredient_measurements = models.ManyToManyField(
        'IngredientMeasurement',
        verbose_name="list of ingredients")


class Ingredient(models.Model):
    name = models.CharField(max_length=250)


class Measurement(models.Model):
    unit = models.CharField(max_length=250)
    system = models.CharField(max_length=250)
    value = models.FloatField()


class IngredientMeasurement(models.Model):
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    measurement = models.ForeignKey('Measurement', on_delete=models.CASCADE)
