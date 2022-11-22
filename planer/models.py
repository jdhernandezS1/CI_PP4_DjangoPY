from django.db import models
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
    day_title = models.CharField(max_length=15, unique=True)
    slugday = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    day_name = models.IntegerField(choices=DAYS_CHOICES, default=0)
    phrase = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['week_owner', 'created_on']


class Meal(models.Model):
    """
    A class for the individual meals
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meal')
    slugmeal = models.SlugField(max_length=30, unique=True)
    meal_description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['owner', 'slugmeal', 'created_on']

    def __str__(self):
        """
        Returns the meal string
        """
        return str(self.slugmeal)

#// COMMANDS TIME
#// save the act day
#  todays_date = datetime.date.today()
#// get the # of the day in the week
# day = todays_date.isoweekday()
