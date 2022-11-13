from django.shortcuts import render,  get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Week
from .forms import *

class PlanerList(generic.ListView):
    """
    A class for the main page "planer index"
    """
    model = Week
    queryset = Week.objects.order_by('-created_on')
    template_name = 'planer_index.html'
    paginate_by = 6
    
    

class WeekList(generic.ListView):
    """
    A class for the Weeks ordered by "created on"
    """
    model = Week
    queryset = Week.objects.filter(status=1).order_by('-created_on')
    template_name = 'planner_index.html'
    paginate_by = 6
# hacer este modificar el request          
# class PlanerDetail(View):
#     """
#     A class for the Post details ordered by "created on"
#     """
#     def get(self, request, title, *args, **kwargs):
#         queryset = Week.objects.filter(status=1)
#         # week = get_object_or_404(queryset, slug=slug)\
#         return render(
#             request,
#             "post_detail.html",
#             {
#                 "post": post,
#                 "comments": comments,
#                 "liked": liked,
#                 "comment_form": CommentForm()
#             },
#         )