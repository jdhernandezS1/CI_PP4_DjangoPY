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


        queryset = Day.objects.filter(status=1)
        post = get_object_or_404(queryset, slugday=slugday)
        mils = post.meals.filter(slugmeal=True).order_by("-created_on")
        meal_form = MealForm(data=request.POST)
        meals = get_list_or_404(Meal, slugmeal="True")
        if meal_form.is_valid():
            meal_form.instance.email = request.user.email
            meal_form.instance.name = request.user.username
            meal = meal_form.save(commit=False)
            meal.post = post
            meal.save()
        else:
            meal_form = MealForm()

        return render(
            request,
            "planer_meal.html",
            {
                "slugday": slugday,
                "mils": mils,
                "meals": meals,
                "meal_form": MealForm
            },
        )
