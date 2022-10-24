from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Week)
class WeekAdmin(SummernoteModelAdmin):

    list_display = ('title', 'weeknumber', 'created_on')
    search_fields = ['title', 'weeknumber']
    list_filter = ('title', 'created_on')
    

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('day_number', 'created_on')
    list_filter = ('day_name', 'created_on')
    search_fields = ('day_name', 'day_number')
    

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('meal', 'meal_number', 'meal_name', 'created_on')
    list_filter = ('meal_number', 'meal_name', 'created_on')
    search_fields = ('meal_number', 'meal_name')
