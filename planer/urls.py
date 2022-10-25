from . import views
from django.urls import path


urlpatterns = [
    path('planer/', views.planer_index.as_view(), name='planer'),
    # path('posts/', views.PostList.as_view(), name='posts'),
    # path('posts/<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    # path('posts/<slug:slug>/like', views.PostLike.as_view(), name="post_like"),
]