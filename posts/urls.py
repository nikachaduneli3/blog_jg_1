from django.urls import path
from . import views
urlpatterns = [
    path('posts/', views.PostListApiView.as_view()),
    path('posts/<int:pk>/', views.PostDetailApiView.as_view()),
    path('posts/<int:pk>/like/', views.like_post),
    path('posts/<int:post_id>/comments', views.CommentsListApiView.as_view()),
]
