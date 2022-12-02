"""
Imports
"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import TestCase
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestHomeViews(TestCase):
    """
    A class for testing exercises views
    """
    def test_get_home_page(self):
        """
        This test checks if the Home page is displayed
        """
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/posts.html')


class TestPostDetailViews(TestCase):
    """
    A class for testing exercises views
    """
    def test_get_postdetail_page(self):
        """
        This test checks if the Post detail page is displayed
        """
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts.html')
