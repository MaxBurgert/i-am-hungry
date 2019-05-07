from django.http import HttpResponse
from django.shortcuts import render

from cookbook.models import Recipe
from .forms import RecipeForm


def get_recipe(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = RecipeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            r = Recipe(
                recipe_name=form.cleaned_data["name"],
                recipe_ingredient=form.cleaned_data["ingredient_main"],
                recipe_source=form.cleaned_data["source"],
            )
            r.save()
            return HttpResponse("Valid input")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RecipeForm()

    return render(request, "recipe.html", {"form": form})


def index(request):
    return render(request, "index.html")
