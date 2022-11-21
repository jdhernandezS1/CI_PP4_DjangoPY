from django.shortcuts import render,  get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Week, Day
from .forms import *


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
    paginate_by = 6
# class PlanerDaily(generic.ListView):
#     """
#     A class for the daily planer "planer_day.html"
#     """
#     def get(self, request, slug, *args, **kwargs):
#         queryset = Week
#         week = get_object_or_404(queryset, slug=slug)
#         day = week.day.order_by('day_name')
#         return render(
#             request,
#             "planer_day.html",
#             {
#                 "week": week,
#                 "day": day,
#                 "slug": slug
#             },
#         )


class Meals(generic.ListView):
    """
    A class for the Weeks ordered by "created on"
    """
    # model = Meal
    # queryset = Meal.objects.order_by('-created_on')
    # template_name = 'planer_meal.html'
    # paginate_by = 6
    def get(self, request, slug, *args, **kwargs):
        queryset = Day
        day = get_object_or_404(queryset, slugday=slug)
        meal = day.meal.order_by('meal_number')
        return render(
            request,
            "planer_meal.html",
            {
                "day":day,
                "meal": meal,
                "edited": True,
                "meal_form": MealForm(),                
                "slug": slug
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Day
        day = get_object_or_404(queryset, slugday=slug)
        meal = day.meal.order_by('meal_number')
        meal_form = MealForm(data=request.POST)
        try:
            if meal_form.is_valid():
                meal_form.instance.email = request.user.email
                meal_form.instance.name = request.user.username
                meal_form.instance.meal_name
                meal_form.instance.meal_description
                dish = meal_form.save(commit=False)
                dish.meal = day
                dish.save()
            else:
                meal_form = MealForm()
        except:
            print("Error")
        return render(
            request,
            "planer_meal.html",
            {
                "day": day,
                "meal": meal,
                "edited": True,
                "meal_form": meal_form,
                "slug": slug
            },
        )
