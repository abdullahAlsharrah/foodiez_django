from django.contrib import admin
from .models import Profile, Recipe, Ingredient, IngredientItem, Step,Category
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(IngredientItem)
admin.site.register(Step)
admin.site.register(Profile)