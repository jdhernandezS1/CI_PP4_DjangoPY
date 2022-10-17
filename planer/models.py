from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from datetime import timedelta

STATUS = ((0, "DRAFT"), (1, "Published"))


class Week(models.Model):
    title = models.CharField(max_length=50, unique=True)
    period = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="week_plan")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Day(models.Model):

    post = models.ForeignKey(Week, on_delete=models.CASCADE, related_name='days')
    day_name = models.CharField(max_length=12)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['created_on']

