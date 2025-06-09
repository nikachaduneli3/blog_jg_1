from django.urls import path
from . import views
urlpatterns = [
    path('posts/', views.PostListApiView.as_view()),
    path('posts/<int:pk>/', views.PostDetailApiView.as_view()),
    path('posts/<int:pk>/like/', views.like_post),
    path('posts/<int:pk>/dislike/', views.dislike_post),
    path('posts/comments/<int:pk>/like/', views.like_comment),
    path('posts/comments/<int:pk>/dislike/', views.dislike_comment),
    path('posts/<int:post_id>/comments/', views.CommentsListApiView.as_view()),
    path('posts/tags/', views.TagListApiView.as_view()),
    path('posts/tags/<int:tag_id>/posts/', views.TagPostsListApiView.as_view()),
    path('posts/categories/', views.CategoryListApiView.as_view()),
    path('posts/categories/<int:category_id>/posts/', views.CategoryPostsListApiView.as_view()),
]
