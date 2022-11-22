from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Week)
class WeekAdmin(SummernoteModelAdmin):
    """
    A class for the weekly section
    """
    list_display = ('title', 'weeknumber', 'created_on')
    search_fields = ['title', 'weeknumber']
    list_filter = ('title', 'created_on')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    """
    A class for the daily section
    """
    list_display = ('day_name', 'created_on')
    list_filter = ('day_name', 'created_on')
    search_fields = ('day_name', 'day_number')
    prepopulated_fields = {'slugday': ('day_title',)}



@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    """
    A class for the meals
    """
    list_display = ('owner','slugmeal', 'created_on')
    list_filter = ('owner','slugmeal', 'created_on')
    search_fields = ('owner', 'slugmeal')
    