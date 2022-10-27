from . import views
from django.urls import path


urlpatterns = [
    path('planer/', views.planer_index.as_view(), name='planer'),
    # path('planer/week/', views.WeekList.as_view(), name='week_list'),
    # path('planer/day/', views.WeekDetail.as_view(), name="days_list"),
    # path('planer/meals/', views.Meals.as_view(), name="meals_list"),
]