from django import forms
from django.contrib.auth import get_user_model

from recipe.models import Ingredient, IngredientItem, Recipe, Step


User = get_user_model()


class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]

        widgets = {
            "password": forms.PasswordInput(),
        }

class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class IngredientItemForm(forms.ModelForm):
    # ingredient = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all())
    # quantity = forms.FloatField()
    class Meta:
        model= IngredientItem
        fields = ['quantity','ingredient','type']

class StepForm(forms.ModelForm):
    class Meta:
        model= Step
        fields = ['name','description']

class RecipeForm(forms.ModelForm):
    class Meta:
        model= Recipe
        fields = ['name','description','image','prep_time','cook_time','serving']

    # def get_ingredients(self, obj):
    #     return obj.get_ingredients()

    # def get_steps(self, obj):
    #     trips = Trip.objects.all()
    #     return t(obj.my_favorite_list(trips))
