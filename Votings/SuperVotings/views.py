from django.shortcuts import render
from SuperVotings.forms import RadioForm

def index(request):
    context = {}
    context['name'] = 'user'
    varinats = ['Putin', 'Trump', 'Xin Jin Pin']
    context['candidates'] = varinats
    if request.method == "POST":
        form = RadioForm(context['candidates'])


    return render(request, 'index.html', context)

def authorization(request):
    return render(request, 'authorization.html')

def restore_page(requset):
    return render(requset, 'restore_page.html')

