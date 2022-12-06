from django.urls import path, include
from accounts.forms import UserLoginForm
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(authentication_form = UserLoginForm), name='login'),
]
