from django.urls import path
from . import views


urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("api/login/", views.LoginAPI.as_view(), name="login-api"),
    path("api/register/", views.RegisterAPI.as_view(), name="register-api"),
    path('home/', views.home, name="home")

]
