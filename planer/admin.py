"""
Imports
"""
# 3rd party:
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
from .models import Meal, Day, Week
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
    list_display = ('title', 'day_name', 'created_on')
    search_fields = ['title', 'day_name', 'day_number']
    list_filter = ('title', 'day_name', 'created_on')
    prepopulated_fields = {'slugday': ('title',)}


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    """
    A class for the meals
    """
    list_display = ('owner', 'title', 'created_on')
    list_filter = ('owner', 'title', 'created_on')
    search_fields = ('owner', 'title')
