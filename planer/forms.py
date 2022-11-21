from django import forms
from .models import Meal


# class MealForm(forms.Form):
#     model = Meal
#     title = forms.CharField(label='meal_name')
#     description = forms.CharField(label= 'meal_description')
class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        prepopulated_fields = {'slugmeal': ('meal_name',)}
        fields = ['meal','meal_name','slugmeal','meal_number','meal_description']



