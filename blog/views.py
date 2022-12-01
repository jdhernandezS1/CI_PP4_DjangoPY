"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render,  get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
# Internal
from .models import Post
from .forms import CommentForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Index(generic.ListView):
    """
    A class for the main page "index"
    """
    model = Post
    template_name = 'index.html'
    paginate_by = 6


class PageNotFound(generic.ListView):
    """
    Page not found Error 404
    """
    model = Post
    # response.status_code = 404 # depend of the library
    template_name = '404.html'
    paginate_by = 6


class PostList(generic.ListView):
    """
    A class for the Blog Post ordered by "created on"
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts.html'
    paginate_by = 6


class PostDetail(View):
    """
    A class for the Post details ordered by "created on"
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Get PostDetail Function
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = {
                "post": post,
                "commented": True,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            }
        return render(
            request,
            "post_detail.html",
            context,
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Post function to comment
        """
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
        context = {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            }
        messages.success(request, 'Your comment was sent')
        return render(
            request,
            "post_detail.html",
            context,
        )


class PostLike(View):
    """
    A class for likes
    """
    def post(self, request, slug, *args, **kwargs):
        """
        Post Likes function
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
