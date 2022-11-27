"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_list_or_404, reverse
from django.shortcuts import get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
# Internal
from .models import Contact
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ContactUs(generic.ListView):
    """
    A class for the main page "planer index"
    """
    model = Contact
    template_name = 'contact_us.html'
