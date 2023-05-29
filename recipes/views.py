from typing import List
from django.shortcuts import render
from django.http import Http404
from django.http.response import HttpResponseRedirect
from .models import Recipes
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import RecipesForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class RecipesDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipes
    success_url = '/smart/recipes'
    template_name = 'recipes/recipes_delete.html'
    login_url = "/login"

class RecipesUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipes
    success_url = '/smart/recipes'
    form_class = RecipesForm
    login_url = "/login"

class RecipesCreateView(LoginRequiredMixin, CreateView):
    model = Recipes
    success_url = '/smart/recipes'
    form_class = RecipesForm
    login_url = "/login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class RecipesListView(LoginRequiredMixin, ListView):
    model = Recipes
    context_object_name = "recipes"
    template_name = "recipes/recipes_list.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.recipes.all()


class RecipesDetailView(LoginRequiredMixin, DetailView):
    model = Recipes
    context_object_name="recipe"
    login_url = "/login"

