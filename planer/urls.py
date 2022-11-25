from . import views
from django.urls import path


urlpatterns = [
    path('planer/week', views.PlanerList.as_view(), name='planer_week'),
    path('planer/', views.PlanerDaily.as_view(), name='planer'),
    path('planer/<slug:slugday>_meals', views.Meals.as_view(), name='meals_list'),
    path('planer/<slug:slugday>_meals/del<int:mealid>', views.DelMeal.as_view(), name='del_meal'),
    # path('planer/day/', views.WeekDetail.as_view(), name="days_list"),
    # path('planer/meals/', views.Meals.as_view(), name="meals_list"),
]