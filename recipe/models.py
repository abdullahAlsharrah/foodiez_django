from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to="profile/",default="")
    bio = models.TextField(default="To change your bio, edit your profile!")

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

class Step(models.Model):
    name =models.CharField(max_length=250,  blank=False)  
    description =models.TextField(default="To change your bio, edit your profile!")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True,related_name="steps")  

