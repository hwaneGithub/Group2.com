from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from players.models import Player


def regPlayer(request) :
	return render(request, 'players/registerPlayer.html')


def regConPlayer(request) :
	club = request.POST['club']
	name = request.POST['name']
	gender = request.POST['gender']
	nname = request.POST['nname']

	qs = Player(p_club=club, p_name=name, p_gender=gender, p_nname=nname)
	qs.save()

	return HttpResponseRedirect(reverse('players:playerAll'))


def reaPlayerAll(request) :
	qs = Player.objects.all()	#선수 정보 가져오기
	context = {'player_list': qs}
	return render(request, 'players/team_manage.html', context)


def detPlayer(request, name) :
	qs = Player.objects.get(p_name = name)
	context = {'player_info': qs}
	return render(request, 'players/detailPlayer.html', context)


def reaPlayerOne(request, name) :
	qs = Player.objects.get(p_name = name)
	context = {'player_info': qs}
	return render(request, 'players/modifyPlayer.html', context)


def modConPlayer(request) :
	pid = request.POST['pid']
	nick = request.POST['nick']
	email = request.POST['email']
	name = request.POST['name']
	birth = request.POST['birth']
	position = request.POST['position']
	team = request.POST['team']

	p_qs = Player.objects.get(p_name = name)	#Query String

	p_qs.p_pid = pid
	p_qs.p_nick = nick
	p_qs.p_email = email
	p_qs.p_name = name
	p_qs.p_birth = birth
	p_qs.p_position = position
	p_qs.p_team = team

	p_qs.save()

	# templates로 이동
	return HttpResponseRedirect(reverse('players:playerAll'))


def delConPlayer(request, id) :
	qs = Player.objects.get(id = id)
	qs.delete()

	return HttpResponseRedirect(reverse('players:playerAll'))