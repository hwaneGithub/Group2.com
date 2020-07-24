from django.urls import path
from . import views

app_name = "match"

urlpatterns = [
    path("my_matlst", views.my_matlst, name='my_matlst'),
    path('<str:date>/match_main/', views.match_main, name='match_main'),
    path('<str:nname>/<int:pk>/matching/', views.matching, name='matching'),
    path('<str:nname>/<int:pk>/delRival/', views.delRival, name='delRival'),
    path('<int:pk>/delMatch/', views.delMatch, name='delMatch'),

    path("reg_match",views.reg_match, name='reg_match'),
    path("create_match", views.create_match, name='create_match'),
]