from django.shortcuts import render,  get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Week
from .forms import *

class planer_index(generic.ListView):
    """
    A class for the main page "planer index"
    """
    model = Week
    template_name = 'planer_index.html'
    paginate_by = 6



class WeekList(generic.ListView):
    """
    A class for the Weeks ordered by "created on"
    """
    model = Week
    queryset = Week.objects.filter(status=1).order_by('-created_on')
    template_name = 'week.html'
    paginate_by = 6
