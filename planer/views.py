"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_list_or_404, reverse
from django.shortcuts import get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
# Internal
from .models import Week, Day, Meal
from .forms import MealForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PlanerList(generic.ListView):
    """
    A class for the main page "planer index"
    """
    model = Week
    template_name = 'planer_index.html'
    paginate_by = 6


class PlanerDaily(generic.ListView):
    """
    A class for the daily planer "planer_day.html"
    """
    model = Day
    template_name = 'planer_day.html'
    paginate_by = 7


class Meals(generic.ListView):
    """
    A class for the Weeks ordered by "created on"
    """
    def get(self, request, slugday, *args, **kwargs):
        if (get_list_or_404(Meal)):
            meals = get_list_or_404(
                Meal,
                slugmeal="True")
            context = {
                "slugday": slugday,
                "meals": meals,
                "meal_form": MealForm()
                }
        else:
            context = {
                "slugday": slugday,
                "meal_form": MealForm()
                }
        return render(
            request,
            "planer_meal.html",
            context,)

    def post(self, request, slugday):
        """
        Creates a new meal
        """
        meal_form = MealForm(request.POST)

        if meal_form.is_valid():
            user = request.user
            meal_form.instance.email = request.user.email
            meal_form.instance.name = request.user.username
            meals = meal_form.save(commit=False)
            meals.owner = user
            meals.save()
            context = {
                "slugday": slugday,
                "meals": meals,
                "meal_form": MealForm
                }

        else:
            meal_form = MealForm()
            context = {
                'meal_form': meal_form
                }
        messages.success(request, 'Meal Was created as well')
        return redirect("planer")


class DelMeal(generic.ListView):
    """
    A clas To Delete meal
    """
    model = Meal

    def post(self, request, slugday, mealid, **kwargs):
        """
        method To Delete meal
        """
        meal = get_object_or_404(Meal, id=mealid)
        meal.delete()
        messages.success(request, 'Meal Was Deleted as well')
        return redirect('meals_list', slugday)


# class EdMeal(generic.ListView):
#     """
#     A clas To Delete meal
#     """
#     model = Meal

#     def post(self, request, slugday, mealid, **kwargs):
#         meal = get_object_or_404(Meal, id=mealid)
#         meal.delete()
#         return redirect('meals_list', slugday)
