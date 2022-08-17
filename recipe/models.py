from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to="profile/",default="")
    bio = models.TextField(default="To change your bio, edit your profile!")
# Currently this model isnt being used, a good place to use signals

class Category(models.Model):
    name = models.CharField(max_length=10,  blank=False)

class Ingredient(models.Model):
    name = models.CharField(max_length=10,  blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,related_name="ingredients")  
   
class Recipe(models.Model):
    name = models.CharField(max_length=250,  blank=False)
    image = models.ImageField(upload_to="recipes/",default="")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True,related_name="recipes")  
    prep_time = models.FloatField()   
    cook_time = models.IntegerField()   
    serving = models.CharField(max_length=250,  blank=False)   
    description = models.TextField(default="To change your bio, edit your profile!")  

class IngredientItem(models.Model):
    types = [
        ("Cup", "Cup"),
        ("Gram", "Gram"),
        ("Liter", "Liter"),
        ("Piece", "Piece"),
    ]
    quantity = models.FloatField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True,related_name="items")  
    type = models.CharField(max_length=10, choices=types, default="cup")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True,related_name="ingredientsItems")  
# This is how i would approach this as well! Great job!
# If you're looking to take this further, you could use a python package for unit validations and conversions
# Check out pint if you're looking to develop this further
# https://pypi.org/project/Pint/
# https://pint.readthedocs.io/en/stable/

class Step(models.Model):
    name =models.CharField(max_length=250,  blank=False)  
    description =models.TextField(default="To change your bio, edit your profile!")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True,related_name="steps")  

