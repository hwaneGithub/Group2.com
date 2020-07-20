from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from teams.models import Team

# Create your views here.
def regTeam(request) :
	return render(request, 'teams/registerTeam.html')

def regConTeam(request) :
	name = request.POST['name']
	major = request.POST['major']
	captain = request.POST['captain']
	memCount = request.POST['memCount']

	qs = Team(t_name=name, t_major=major, t_captain=captain, t_memCount=memCount)
	qs.save()

	return HttpResponseRedirect(reverse('teams:teamAll'))

def reaTeamAll(request) :
	qs = Team.objects.all()	#팀 정보 가져오기
	context = {'team_list': qs}
	return render(request, 'teams/readTeam.html', context)

def detTeam(request, name) :
	qs = Team.objects.get(t_name = name)
	context = {'team_info': qs}
	return render(request, 'teams/detailTeam.html', context)

def reaTeamOne(request, name) :
	qs = Team.objects.get(t_name = name)
	context = {'team_info': qs}
	return render(request, 'teams/modifyTeam.html', context)

def modConTeam(request) :
	name = request.POST['name']
	major = request.POST['major']
	captain = request.POST['captain']
	memCount = request.POST['memCount']

	t_qs = Team.objects.get(t_name = name)	#Query String

	t_qs.t_name = name
	t_qs.t_major = major
	t_qs.t_captain = captain
	t_qs.t_memCount = memCount

	t_qs.save()

	# templates로 이동
	return HttpResponseRedirect(reverse('teams:teamAll'))

def delConTeam(request, name) :
	qs = Team.objects.get(t_name = name)
	qs.delete()

	return HttpResponseRedirect(reverse('teams:teamAll'))