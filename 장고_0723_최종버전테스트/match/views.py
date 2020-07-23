from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.


@login_required(login_url='user:login')
def my_matlst(request):
    return render(request, 'my_matchlist.html')
