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

app_name = 'teams' #앞에 만든 urls를 찾기 쉽게 app_name이라는 변수 생성.
urlpatterns = [
	# url이 teams reg로 들어왔을 때 view에 있는 regTeam함수를 실행하라는 명령


	path('reg/', views.regTeam, name='reg'),
	path('regCon/', views.regConTeam, name='regCon'),
	path('all/', views.reaTeamAll, name='teamAll'),
	path('<int:id>/det/', views.detTeam, name='teamDet'), # team_id는 앞에서 받은 t.id를 넣어주는 자리임(뭐라쓰던 중요x)
	path('<int:id>/mod/', views.reaTeamOne, name='teamMod'),
	path('modCon/', views.modConTeam, name='modCon'),
	path('<int:id>/del/', views.delConTeam, name='teamDel'),



	path('recruit/', views.recruitAll, name='recruitAll'),
	path('recruit/reg/', views.recruitNew, name='recruitNew'),
	path('recruit/regCon/', views.recruitCon, name='recruitCon'),
	path('recruit/<int:id>/det/', views.recruitDet, name='recruitDet'),
	path('recruit/<int:id>/mod/', views.recruitOne, name='recruitMod'),
	path('recruit/modCon/', views.modRecruit, name='recmodCon'),
	path('recruit/<int:id>/del/', views.delConRecruit, name='recruitDel'),
	path('comment/<int:id>/<int:r_id>/del/', views.commentDel, name='commentDel'),
]
