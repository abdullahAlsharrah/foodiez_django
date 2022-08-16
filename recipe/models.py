from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=10,  blank=False)

class Ingredient(models.Model):
    name = models.CharField(max_length=10,  blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,related_name="ingredients")  
   
class Recipe(models.Model):
    name = models.CharField(max_length=250,  blank=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    prep_time = models.FloatField()   
    cook_time = models.IntegerField()   
    serving = models.CharField(max_length=250,  blank=False)   
    description = models.CharField(max_length=250,  blank=False)  

class IngredientItem(models.Model):
    quantity = models.IntegerField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True,related_name="items")  
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True,related_name="ingredientsItems")  
