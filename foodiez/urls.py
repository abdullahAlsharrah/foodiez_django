
from django.contrib import admin
from django.urls import path
from recipe import views as recipe_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth pages
    path('registration/', recipe_views.registration_view, name="registration"),
    path('login/', recipe_views.user_login, name="login"),
    path('logout/', recipe_views.logout_view, name="logout"),

    # Home
    path('', recipe_views.home, name="home"),

    # Recipes
    path('recipes/', recipe_views.recipes_view, name="recipes"),
    path('recipes/<int:ingredient_id>', recipe_views.filtered_recipes_view, name="filtered_recipes"),
    path('recipes/chef/<int:chef_id>', recipe_views.chef_recipes_view, name="chef_recipes"),
    path('recipes/chef/<int:chef_id>/<int:ingredient_id>', recipe_views.chef_filtered_recipes_view, name="chef_filterd_recipes"),
    path('recipe/detail/<int:recipe_id>/', recipe_views.recipe_detail_view, name="recipe_detail"),

    # Ingredients
    path('categories', recipe_views.categories_view, name="categories"),
    path('ingredients/<int:category_id>', recipe_views.ingredients_view, name="ingredients"),

    # Chefs
    path('chefs', recipe_views.chefs_view, name="chefs"),
    path('my_profile', recipe_views.my_recipes_view, name="my_profile"),


    #Create
    path('new_recipe/', recipe_views.create_reciepe, name="new_recipe"),
]
handler404 = 'recipe.views.handler404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)