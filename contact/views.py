"""
Imports
"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
# Internal
from .models import Contact
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ContactUs(generic.ListView):
    """
    A class for the main page "planer index"
    """
    model = Contact
    template_name = 'contact_us.html'

    def get(self, request, *args, **kwargs):
        """
        Contact us Form
        """
        return render(
            request,
            "contact_us.html",
            )

    def post(self, request, *args, **kwargs):
        """
        Contact Us Post method
        """
        messages.success(request, 'Your message was send')
        return redirect("home")
