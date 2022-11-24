from django import forms
from .models import Meal


# class MealForm(forms.Form):
#     model = Meal
#     title = forms.CharField(label='meal_name')
#     description = forms.CharField(label= 'meal_description')
class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ('title', 'day', 'meal_description', 'featured_image')


class DelMealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ('slugmeal',)
