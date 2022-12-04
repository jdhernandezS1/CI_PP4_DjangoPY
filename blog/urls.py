"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path
# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('403', views.ServerDeniesAcces.as_view(), name='403'),
    path('404', views.PageNotFound.as_view(), name='404'),
    path('500', views.InternalServerError.as_view(), name='500'),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('posts/<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    path('posts/<slug:slug>/like', views.PostLike.as_view(), name="post_like"),
]
