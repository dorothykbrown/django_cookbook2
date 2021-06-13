from django.shortcuts import render
from .models import Recipe
# Create your views here.


def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'cookbook/all_recipes.html', {'recipes': recipes})
