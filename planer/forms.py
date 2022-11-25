"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Meal


class MealForm(forms.ModelForm):
    """
    A class for form to create a meal
    """
    class Meta:
        """
        To order items
        """
        model = Meal
        fields = ('title', 'day', 'meal_description')


class DelMealForm(forms.ModelForm):
    """
    A class for form to delete a meal
    """
    class Meta:
        """
        To order items
        """
        model = Meal
        fields = ('slugmeal',)
