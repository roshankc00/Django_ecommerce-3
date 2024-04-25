
from django.urls import path,include
from .views import UserRegistrationView,UserLoginView
urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name="register user"),
    path('login/',UserLoginView.as_view(),name="login user")
]
