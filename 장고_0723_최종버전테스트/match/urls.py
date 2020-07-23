from django.urls import path
from . import views

app_name = "match"

urlpatterns = [
    path("my_matlst", views.my_matlst, name='my_matlst'),
    path('<str:date>/match_main/', views.match_main, name='match_main')
]