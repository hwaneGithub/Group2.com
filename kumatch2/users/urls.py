from django.urls import path
from . import views
from users.views import BoardListView, BoardDetailView, BoardCreateUpdateView

app_name = "user"

urlpatterns = [
    path("", views.main, name="main"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path('board/', BoardListView.as_view(), name="board_main"), # as_view메소드는 간단하게 설명하면 뷰클래스의 초기화와 핸들러를 반환하는 기능을 제공
	path('board/create/', BoardCreateUpdateView.as_view()),
	path('board/<board_id>/', BoardDetailView.as_view()),
	path('board/<board_id>/update/', BoardCreateUpdateView.as_view()),
]