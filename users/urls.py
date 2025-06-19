from django.urls import path
from .views import RegisterUser, activate_user, ProfileApiView

urlpatterns = [
    path('register/', RegisterUser.as_view()),
    path('activate/<str:uid>/<str:token>', activate_user),
    path('profile/', ProfileApiView.as_view())
]

