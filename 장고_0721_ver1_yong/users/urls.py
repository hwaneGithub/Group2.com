from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("", views.main, name="main"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("notice",views.notice_view, name="notice"),
    path("manage", views.manage_view, name="manage"),
    path("intro", views.intro_view, name="intro"),
]
