from django.shortcuts import render, redirect
from recipes.recipes_app.forms import RecipeForm
from recipes.recipes_app.models import Recipe

# Create your views here.


def index(request):
    all_recipes = Recipe.objects.all()
    context = {
        'recipes': all_recipes
    }
    return render(request, 'index.html', context)


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')

    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'details.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    else:
        form = RecipeForm()

    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
        return redirect('index')

    else:
        form = RecipeForm(instance=recipe)

    context = {
        'form': form
    }
    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('index')

    form = RecipeForm(initial=recipe.__dict__)
    for field in form.fields:
        form.fields[field].disabled = True

    context = {
        'form': form
    }
    return render(request, 'delete.html', context)
