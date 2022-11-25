"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
# integerfield choices
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
    weeknumber = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="week"
    )
    status = models.IntegerField(
        choices=STATUS,
        default=0
        )
    title = models.CharField(
        max_length=15,
        unique=True
        )
    slug = models.SlugField(
        max_length=200,
        unique=True
        )
    period = models.DateTimeField()
    updated_on = models.DateTimeField(
        auto_now=True
        )
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    featured_image = CloudinaryField(
        'image',
        default='placeholder'
        )

    class Meta:
        """
        Items Order
        """
        ordering = [
            '-created_on',
            'weeknumber'
            ]

    def __str__(self):
        return str(self.title)


class Day(models.Model):
    """
    A class for the Day
    """
    week_owner = models.ForeignKey(
        Week,
        on_delete=models.CASCADE,
        default=0,
        related_name="day"
    )
    title = models.CharField(
        max_length=15,
        unique=True
    )
    slugday = models.SlugField(
        max_length=200,
        unique=True
        )
    day_name = models.IntegerField(
        choices=DAYS_CHOICES,
        default=0
        )
    phrase = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    featured_image = CloudinaryField(
        'image',
        default='placeholder'
        )
    status = models.IntegerField(
        choices=STATUS,
        default=1
        )

    class Meta:
        """
        Items Order
        """
        ordering = ['week_owner', 'created_on']


class Meal(models.Model):
    """
    A class for the individual meals
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='meals'
        )
    day = models.CharField(
        choices=MEAL_DAY_CHOICES,
        max_length=20,
        default="monday")
    title = models.CharField(
        max_length=20
        )
    slugmeal = models.BooleanField(
        default=True
        )
    meal_description = models.TextField()
    featured_image = CloudinaryField(
        'image',
        default='placeholder'
        )
    created_on = models.DateTimeField(
        auto_now_add=True
        )

    class Meta:
        """
        Items order
        """
        ordering = [
            'owner',
            'title',
            'created_on']

    def __str__(self):
        """
        Returns the meal string
        """
        return str(self.slugmeal)
