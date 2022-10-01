from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("profile/<int:stall_id>", views.profile, name="profile")
]