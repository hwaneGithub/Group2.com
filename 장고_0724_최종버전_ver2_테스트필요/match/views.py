from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from match.models import Match


# Create your views here.


@login_required(login_url='user:login')
def my_matlst(request):
    qs = Match.objects.all()
    context = {'match_list': qs}
    return render(request, 'my_matchlist.html', context)


@login_required(login_url='user:login')
def match_main(request, date):
    qs = Match.objects.filter(m_date=date)
    context = {'match_list': qs}
    return render(request, 'match_main.html', context)


def matching(request, nname, pk):
    qs = Match.objects.get(pk=pk)
    qs.m_rival = nname
    qs.save()
    return render(request, 'match_main.html')


def delRival(request, nname, pk):
    qs = Match.objects.get(pk=pk)
    qs.m_rival = ''
    qs.save()
    return render(request, 'match_main.html')


def delMatch(request, pk):
    qs = Match.objects.get(pk=pk)
    qs.delete()
    return render(request, 'match_main.html')


def reg_match(request):
    return render(request, 'match_register.html')


def create_match(request):
    date = request.POST['m_date']
    time = request.POST['time']
    place = request.POST['place']
    nname = request.POST['nname']
    gender = request.POST['gender']
    num = request.POST['num']

    qs = Match(m_date=date, m_time=time, m_place=place, m_nname=nname, m_gender=gender, m_num=num)
    qs.save()
    return HttpResponseRedirect(reverse('match:my_matlst'))
