
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

    #Home
    path('', recipe_views.home, name="home"),
    path('recipes/', recipe_views.recipes_view, name="recipes"),
    path('recipe/detail/<int:recipe_id>/', recipe_views.recipe_detail_view, name="recipe_detail"),
    path('categories', recipe_views.categories_view, name="catgeories"),
]
handler404 = 'recipe.views.handler404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)