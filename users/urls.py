from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings

from . import views

app_name= 'users'

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},name="logout"),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]


