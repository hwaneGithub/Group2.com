from django.shortcuts import render


# Create your views here.

def my_matlst(request):
    return render(request, 'my_matchlist.html')
