from django.urls import path, include
from accounts.forms import UserLoginForm
from accounts.views import RegisterView, edit_profile
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(authentication_form = UserLoginForm), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', edit_profile, name='profile'),
]
