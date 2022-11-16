from django.shortcuts import render,  get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

class PlanerList(generic.ListView):
    """
    A class for the main page "planer index"
    """
    model = Week
    queryset = Week.objects.order_by('-created_on')
    template_name = 'planer_index.html'
    paginate_by = 6
    
class PlanerDaily(generic.ListView):
    """
    A class for the daily planer "planer_day.html"
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Week.objects.filter(status=1)
        week = get_object_or_404(queryset, slug=slug)
        day = week.day.order_by('day_name')
        return render(
            request,
            "planer_day.html",
            {
                "week": week,
                "day": day,
                "slug": slug
            },
        )

class Meals(generic.ListView):
    """
    A class for the Weeks ordered by "created on"
    """
    # model = Meal
    # queryset = Meal.objects.order_by('-created_on')
    # template_name = 'planer_meal.html'
    # paginate_by = 6
    def get(self, request, slug, *args, **kwargs):
        queryset = Day.objects
        day = get_object_or_404(queryset, slugday=slug)
        meal = day.meal.order_by('meal_number')
        return render(
            request,
            "planer_meal.html",
            {
                "meal": meal,
                "slug": slug
            },
        )
