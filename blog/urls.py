from . import views
from django.urls import path

# handler404 = "blog.views.page_not_found"
urlpatterns = [
    path('', views.index.as_view(), name='home'),
    path('404', views.page_not_found.as_view(), name='404'),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('posts/<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    path('posts/<slug:slug>/like', views.PostLike.as_view(), name="post_like"),
]