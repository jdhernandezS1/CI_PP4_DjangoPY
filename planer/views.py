from django.shortcuts import render, get_list_or_404, reverse, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Week, Day, Meal
from .forms import MealForm


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
    # model = Meal
    # queryset = Meal.objects.order_by('-created_on')
    # template_name = 'planer_meal.html'
    # paginate_by = 6
    def get(self, request, slugday, *args, **kwargs):
        meals = get_list_or_404(Meal, slugmeal="True")
        return render(request, "planer_meal.html", {
            "slugday": slugday,
            "meals": meals,
            "meal_form": MealForm()
                },
                )

    def post(self, request, slugday, *args, **kwargs):

        meals = get_list_or_404(Meal, slugmeal="True")

        queryset = Day.objects
        post = get_object_or_404(queryset, slugday=slugday)
        meal_form = MealForm(data=request.POST)
        if meal_form.is_valid():
            meal_form.instance.email = request.user.email
            meal_form.instance.name = request.user.username
            meal_form.save()
            dish = meal_form.save(commit=False)
            dish.day = post
            dish.save()
        else:
            meal_form = MealForm()

        return render(
            request,
            "planer_meal.html",
            {
                "slugday": slugday,
                "meals": meals,
                "meal_form": MealForm
            },
        )
