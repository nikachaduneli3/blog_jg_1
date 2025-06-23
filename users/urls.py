from django.urls import path
from .views import(
    RegisterUser,
    activate_user,
    ProfileApiView,
    UsersListApiView,
    UsersDetailView,
    UsersPostsView
)

urlpatterns = [
    path('register/', RegisterUser.as_view()),
    path('activate/<str:uid>/<str:token>', activate_user),
    path('profile/', ProfileApiView.as_view()),
    path('', UsersListApiView.as_view()),
    path('<int:pk>/', UsersDetailView.as_view()),
    path('<int:author_id>/posts/', UsersPostsView.as_view()),
]

