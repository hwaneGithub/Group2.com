from django.urls import path, include
from . import views
from users.views import BoardListView, BoardDetailView, BoardCreateUpdateView

app_name = "user"

urlpatterns = [
    path("", views.main, name="main"),
    path("", include('teams.urls')),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
]
