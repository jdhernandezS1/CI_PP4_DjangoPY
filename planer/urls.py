"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path
# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


urlpatterns = [
    path(
        'planer/week',
        views.PlanerList.as_view(),
        name='planer_week'
        ),
    path(
        'planer/',
        views.PlanerDaily.as_view(),
        name='planer'
        ),
    path(
        'planer/<slug:slugday>_meals',
        views.Meals.as_view(),
        name='meals_list'
        ),
    path(
        'planer/<slug:slugday>_meals/del<int:mealid>',
        views.DelMeal.as_view(),
        name='del_meal'
        ),
    path(
        'planer/<slug:slugday>_meals/edit<int:mealid>',
        views.EdMeal.as_view(),
        name='ed_meal'
        ),
        ]
