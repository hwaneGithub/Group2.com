"""tempPjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views # . 아무거나 들어와도 views

app_name = 'players' #앞에 만든 urls를 찾기 쉽게 app_name이라는 변수 생성.
urlpatterns = [
	# url이 players reg로 들어왔을 때 view에 있는 regPlayer함수를 실행하라는 명령
	path('reg/', views.regPlayer, name='reg'),
	path('regCon/', views.regConPlayer, name='regCon'),
	path('all/', views.reaPlayerAll, name='playerAll'),
	path('<str:name>/det/', views.detPlayer, name='playerDet'),
	path('<str:name>/mod/', views.reaPlayerOne, name='playerMod'),
	path('modCon/', views.modConPlayer, name='modCon'),
	path('<str:name>/del/', views.delConPlayer, name='playerDel'),
]
