import re
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from recipe.forms import IngredientItemForm, RecipeForm, StepForm, UserLogin, UserRegister
from recipe.models import Category, Ingredient, IngredientItem, Profile, Recipe, Step
from django.forms.models import inlineformset_factory


# Create your views here.
def handler404(request,exception):
    return render(request,"404.html")
    
def home(request):

    categories = {category: Ingredient.objects.filter(category = category) for category in Category.objects.all()}

    recipes: list[Recipe] = list(Recipe.objects.all())
    context = {
        "recipes": recipes,
                "categories":categories

    }
    return render(request,'home.html',context)

def registration_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            # Save the object user  
            user = form.save(commit=False)
            # hashing the password
            user.set_password(user.password)
            user.save()

            login(request,user)

            return redirect("home")
    context={
        "form":form,
    }
    return render(request,'registration.html',context)

def user_login(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect("home")

    context = {
        "form": form,
    }
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("registration")

def recipes_view(request):
    recipes: list[Recipe] = list(Recipe.objects.all())
    categories = {category: Ingredient.objects.filter(category = category) for category in Category.objects.all()}
    context = {
        "recipes": recipes,
        "categories":categories
    }
    return render(request, "recipes_page.html",context)

def filtered_recipes_view(request,ingredient_id):
    recipes = []
    ingredientsItem = IngredientItem.objects.filter(ingredient_id=ingredient_id)
    ingredient = Ingredient.objects.get(id=ingredient_id)
    categories = {category: Ingredient.objects.filter(category = category) for category in Category.objects.all()}
    for i in ingredientsItem:
        if i.recipe:
                recipes.append(i.recipe)
    context = {
        "recipes": recipes,
        "categories":categories,
        'ingredient':ingredient
    }
    return render(request, "recipes_page.html",context)

def chef_recipes_view(request,chef_id):
    recipes: list[Recipe] = list(Recipe.objects.filter(profile=chef_id))
    profile = Profile.objects.get(user_id= chef_id)
    categories = {category: Ingredient.objects.filter(category = category) for category in Category.objects.all()}

    context = {
        "recipes": recipes,
        'chef':profile,
        "categories":categories

    }
    return render(request, "recipes_page.html",context)

def my_recipes_view(request):
    recipes: list[Recipe] = list(Recipe.objects.filter(profile=request.user.id))
    profile = Profile.objects.get(user_id= request.user.id)
    categories = {category: Ingredient.objects.filter(category = category) for category in Category.objects.all()}

    context = {
        "recipes": recipes,
        'chef':profile,
        "categories":categories

    }
    return render(request, "recipes_page.html",context)

def chef_filtered_recipes_view(request,chef_id,ingredient_id):
    recipes=[]
    ingredientsItem = IngredientItem.objects.filter(ingredient_id=ingredient_id )
    ingredient = Ingredient.objects.get(id=ingredient_id)

    for i in ingredientsItem:
        if i.recipe and i.recipe.profile.user.id == chef_id:
                recipes.append(i.recipe)
    profile = Profile.objects.get(user_id= chef_id)
    categories = {category: Ingredient.objects.filter(category = category) for category in Category.objects.all()}

    context = {
        "recipes": recipes,
        'chef':profile,
        "categories":categories,
        'ingredient':ingredient
    }
    return render(request, "recipes_page.html",context)

def chefs_view(request):
    profiles: list[Profile] = list(Profile.objects.all())
    
    context = {
        "profiles": profiles,
    }
    return render(request, "profiles.html",context)

def recipe_detail_view(request,recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients: list[IngredientItem] = list(IngredientItem.objects.filter(recipe_id = recipe.id))
    steps: list[Step] = list(Step.objects.filter(recipe_id = recipe.id))
    
    context={
        'recipe':recipe,
        'ingredients':ingredients,
        'steps':steps
    }
    return render(request, "recipe_details.html",context)

def categories_view(request):
    # categories: list[Category] = list(Category.objects.all())
    categories = {category: Ingredient.objects.filter(category = category) for category in Category.objects.all()}

    context={
        'categories':categories,
    }
    return render(request, "categories.html",context)

def ingredients_view(request,category_id):
    # categories: list[Category] = list(Category.objects.all())
    categories = {ingredient: IngredientItem.objects.filter(ingredient = ingredient) for ingredient in Ingredient.objects.filter(category_id=category_id)}

    context={
        'categories':categories,
        'ingredients_view':True
    
    }
    return render(request, "categories.html",context)

# Create Recipe
@login_required
def create_reciepe(request):
    form = RecipeForm()
    ingredientItemForm = inlineformset_factory(model= IngredientItem,parent_model=Recipe, form=IngredientItemForm,extra=0)
    stepForm = inlineformset_factory(model= Step,parent_model=Recipe, form=StepForm,extra=0)
    formSet = ingredientItemForm()
    formSet_steps = stepForm()
    if request.method == "POST":
        form = RecipeForm(request.POST,request.FILES)
        formSet = ingredientItemForm(request.POST)
        formSet_steps = stepForm(request.POST)
        if all([form.is_valid(),formSet.is_valid(),formSet_steps.is_valid()]):
            parent = form.save(commit=False)
            parent.profile = request.user.profile
            parent.save()
            print(formSet)
            for form in formSet:
                child = form.save(commit=False)
                child.recipe = parent
                child.save()
            for form in formSet_steps:
                child = form.save(commit=False)
                child.recipe = parent
                child.save()
            return redirect("recipes")
    context = {
        "form": form,
        "ingredient_form":formSet,
        'step_form':formSet_steps
    }
    return render(request,'creare_recipe.html',context)