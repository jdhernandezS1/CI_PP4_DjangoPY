from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# import datetime


STATUS = ((0, "DRAFT"), (1, "Published"))


class Week(models.Model):
    """
    A class for the weekly meals
    """

    title = models.CharField(max_length=15, unique=True)
    period = models.DateTimeField()
    weeknumber = models.ForeignKey(User, on_delete=models.CASCADE, related_name="week")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-created_on', 'weeknumber']

    def __str__(self):
        return self.title


class Day(models.Model):
    """
    A class for the daily meals
    """

    day_name = models.CharField(max_length=9, unique=True)
    day_number = models.ForeignKey(Week, on_delete=models.CASCADE, related_name='day')
    phrase = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['day_number', 'created_on']


class Meal(models.Model):
    """
    A class for the individual meals
    """

    meal = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='meal')
    meal_number = models.DecimalField(decimal_places=0,max_digits=1, unique=True)
    meal_name = models.CharField(max_length=30)
    meal_description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['meal_number', 'created_on']
    
    def __str__(self):
        """
        Returns the meal string
        """
        return self.meal_name

#// COMMANDS TIME
#// save the act day
#  todays_date = datetime.date.today()
#// get the # of the day in the week
# day = todays_date.isoweekday()
