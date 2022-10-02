from . import views
from django.urls import path


urlpatterns = [
    path('', views.index.as_view(), name='home'),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('posts/<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    path('posts/<slug:slug>/like', views.PostLike.as_view(), name="post_like"),
]
