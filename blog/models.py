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


STATUS = (
    (0, "DRAFT"),
    (1, "Published")
    )


class Post(models.Model):
    """
    A class for Post model
    """
    title = models.CharField(
        max_length=200,
        unique=True
        )
    slug = models.SlugField(
        max_length=200,
        unique=True
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts"
        )
    updated_on = models.DateTimeField(
        auto_now=True
        )
    content = models.TextField()
    featured_image = CloudinaryField(
        'image',
        default='placeholder'
        )
    exerpt = models.TextField(
        blank=True
        )
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    status = models.IntegerField(
        choices=STATUS,
        default=0
        )
    likes = models.ManyToManyField(
        User,
        related_name='blog_likes',
        blank=True
        )

    class Meta:
        """
        Items Order
        """
        ordering = [
            '-created_on'
            ]

    def __str__(self):
        """
        Return Title
        """
        return str(self.title)

    def number_of_likes(self):
        """
        Likes Counter
        """
        return self.likes.count()
        # is valid method but the validator doesnt allow it


class Comment(models.Model):
    """
    A class for Comment Model
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
        )
    name = models.CharField(
        max_length=80
        )
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    approved = models.BooleanField(
        default=True
        )

    class Meta:
        """
        Items Order
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment{self.body} by {self.name}"
