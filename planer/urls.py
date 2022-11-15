from . import views
from django.urls import path


urlpatterns = [
    path('planer/', views.PlanerList.as_view(), name='planer'),
    path('planer/<slug:slug>', views.PlanerDaily.as_view(), name='planer_day'),
    # path('planer/week/', views.WeekList.as_view(), name='week_list'),
    # path('planer/day/', views.WeekDetail.as_view(), name="days_list"),
    # path('planer/meals/', views.Meals.as_view(), name="meals_list"),
]