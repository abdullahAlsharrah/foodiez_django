from django import forms
from django.contrib.auth import get_user_model

from recipe.models import IngredientItem, Recipe, Step


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

class IngredientItemForm(forms.Form):
    class Meta:
        model= IngredientItem
        fields = ['quantity','ingrediant']

class StepForm(forms.Form):
    class Meta:
        model= Step
        fields = ['name','description']

class RecipeForm(forms.Form):
    ingredients = IngredientItemForm()
    steps =StepForm()
    class Meta:
        model= Recipe
        fields = ['name','description','ingredients','image','prep_time','cook_time','serving','steps']
