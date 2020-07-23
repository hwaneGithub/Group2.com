from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from match.models import Match


# Create your views here.


@login_required(login_url='user:login')
def my_matlst(request):
    return render(request, 'my_matchlist.html')


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
