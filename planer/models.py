from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# import datetime


STATUS = ((0, "DRAFT"), (1, "Published"))
monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6
sunday = 7
DAYS_CHOICES = (
    (monday, 'monday'),
    (tuesday, 'tuesday'),
    (wednesday, 'wednesday'),
    (thursday, 'thursday'),
    (friday, 'friday'),
    (saturday, 'saturday'),
    (sunday, 'sunday'),
)
breakfast = 1
lunch = 2
dinner = 3

MEAL_CHOICES = (
    (breakfast, 'breakfast'),
    (lunch, 'lunch'),
    (dinner, 'dinner'),
)
MEAL_DAY_CHOICES = (
    ("monday", 'monday'),
    ("tuesday", 'tuesday'),
    ("wednesday", 'wednesday'),
    ("thursday", 'thursday'),
    ("friday", 'friday'),
    ("saturday", 'saturday'),
    ("sunday", 'sunday'),
)


class Week(models.Model):
    """
    A class for the weekly meals
    """
    weeknumber = models.ForeignKey(User, on_delete=models.CASCADE, related_name="week")
    status = models.IntegerField(choices=STATUS, default=0)
    title = models.CharField(max_length=15, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    period = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-created_on', 'weeknumber']

    def __str__(self):
        return str(self.title)


class Day(models.Model):
    """
    A class for the daily meals
    """
    week_owner = models.ForeignKey(Week, on_delete=models.CASCADE, default=0, related_name="day")
    title = models.CharField(max_length=15, unique=True)
    slugday = models.SlugField(max_length=200, unique=True)
    day_name = models.IntegerField(choices=DAYS_CHOICES, default=0)
    phrase = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['week_owner', 'created_on']


class Meal(models.Model):
    """
    A class for the individual meals
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')
    day = models.CharField(choices=MEAL_DAY_CHOICES, max_length=20, default="monday")
    title = models.CharField(max_length=20, unique=True)
    slugmeal = models.BooleanField(default=True)
    meal_description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['owner', 'title', 'created_on']

    def __str__(self):
        """
        Returns the meal string
        """
        return str(self.slugmeal)


class MealPlan(models.Model):
    """
    Class for the MealPlan model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meal_plan')
    meal = models.DateField()

    class Meta:
        """
        Internal Class to order and give contraint s
        """
        ordering = ['meal']
        constraints = [UniqueConstraint(fields=['user', 'meal'], name='meal_id')]

    def __str__(self):
        """
        Return meal
        """
        return (self.meal)


class food(models.Model):
    """
    Class food model
    """
    food_name = models.CharField(max_length=10, blank=True, null=False, default=' ')
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE, related_name='plan')
    description = models.DateField()

    def __str__(self):
        """
        Returns the workout name string
        """
        return self.food_name