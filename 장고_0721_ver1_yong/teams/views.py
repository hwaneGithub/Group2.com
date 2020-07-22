from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from teams.models import Team
from teams.models import Recruit


# Create your views here.
def regTeam(request):
    return render(request, 'teams/board_create.html')


def regConTeam(request):
    name = request.POST['name']
    major = request.POST['major']
    captain = request.POST['captain']
    memCount = request.POST['memCount']

    qs = Team(t_name=name, t_major=major, t_captain=captain, t_memCount=memCount)
    qs.save()

    return HttpResponseRedirect(reverse('teams:teamAll'))


def reaTeamAll(request):
    qs = Team.objects.all()  # 팀 정보 가져오기
    context = {'team_list': qs}
    return render(request, 'teams/board_main_ver2.html', context)


def detTeam(request, id):
    qs = Team.objects.get(id=id)
    context = {'team_info': qs}
    return render(request, 'teams/board_detail.html', context)


def reaTeamOne(request, id):
    qs = Team.objects.get(id=id)
    context = {'team_info': qs}
    return render(request, 'teams/board_update.html', context)


def modConTeam(request):
    name = request.POST['name']
    major = request.POST['major']
    captain = request.POST['captain']
    memCount = request.POST['memCount']
    id = request.POST['id']

    t_qs = Team.objects.get(id=id)  # Query String

    t_qs.t_name = name
    t_qs.t_major = major
    t_qs.t_captain = captain
    t_qs.t_memCount = memCount

    t_qs.save()

    # templates로 이동
    return HttpResponseRedirect(reverse('teams:teamAll'))


def delConTeam(request, id):
    qs = Team.objects.get(id=id)
    qs.delete()

    return HttpResponseRedirect(reverse('teams:teamAll'))


def recruitAll(request):
    qs = Recruit.objects.all()  # 팀 정보 가져오기
    context = {'recruit_list': qs}
    return render(request, 'teams/board2_main.html', context)
