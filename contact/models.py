"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Contact(models.Model):
    """
    A class for Post model
    """
    title = models.CharField(
        max_length=100
        )
    author = models.EmailField(
        max_length=30
        )
    content = models.TextField()

    class Meta:
        """
        Items Order
        """
        ordering = [
            '-title'
            ]

    def __str__(self):
        """
        Return Title
        """
        return str(self.title)
