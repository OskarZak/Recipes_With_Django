from django.urls import path
from . import views

urlpatterns = [
    path('recipes', views.RecipesListView.as_view(), name="recipes.list"),
    path('recipes/<int:pk>', views.RecipesDetailView.as_view(), name="recipes.detail"),
    path('recipes/<int:pk>/edit', views.RecipesUpdateView.as_view(), name="recipes.update"),
    path('recipes/<int:pk>/delete', views.RecipesDeleteView.as_view(), name="recipes.delete"),
    path('recipes/new', views.RecipesCreateView.as_view(), name="recipes.new"),
    

]