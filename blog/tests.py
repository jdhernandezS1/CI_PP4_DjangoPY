"""
Imports
"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import RequestFactory, TestCase
from .views import Index, PostList
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class HomePageTest(TestCase):
    """
    Home Page Test
    """
    def test_environment_set_in_context(self):
        """
        Home page Test
        """
        request = RequestFactory().get('')
        view = Index()
        view.setup(request)


class ForoPageTest(TestCase):
    """
    Foro Page Test
    """
    def test_environment_set_in_context(self):
        """
        Post
        """
        request = RequestFactory().get('/posts/')
        view = PostList()
        view.setup(request)
