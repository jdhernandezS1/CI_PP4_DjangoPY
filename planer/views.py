from django.shortcuts import render,  get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

class PlanerList(generic.ListView):
    """
    A class for the main page "planer index"
    """
    model = Week
    queryset = Week.objects.order_by('-created_on')
    template_name = 'planer_index.html'
    paginate_by = 6
    
class PlanerDaily(generic.ListView):
    """
    A class for the daily planer "planer_day.html"
    """
    # model = Day
    # queryset = Day.objects.order_by('-created_on')
    # template_name = 'planer_day.html'
    def get(self, request, title, *args, **kwargs):
        queryset = Week.objects.filter(status=1)
        week = get_object_or_404(queryset, title=title)

        return render(
            request,
            "planer_day.html",
            {
                "title": title
            },
        )

class meals(generic.ListView):
    """
    A class for the Weeks ordered by "created on"
    """
    model = Week
    queryset = Week.objects.filter(status=1).order_by('-created_on')
    template_name = 'planner_index.html'
    paginate_by = 6
    def post(self, request, slug, *args, **kwargs):
        
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )
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