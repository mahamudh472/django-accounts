from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.loginView, name="login"),
    path('signup/', views.signup ,  name="signup")
]   