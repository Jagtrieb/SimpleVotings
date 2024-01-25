import random
from django.shortcuts import render
from SuperVotings.forms import RadioForm

from SuperVotings.models import Vote


def index(request):
    context = {}
    context['name'] = 'user'



    return render(request, 'index.html', context)

def authorization(request):
    return render(request, 'authorization.html')

def restore_page(requset):
    return render(requset, 'restore_page.html')

def signup(request):
    return render(request, 'signup.html')

def voting_page(requset):
    context = {}
    varinats = ['Putin', 'Trump', 'Xin Jin Pin']
    context['candidates'] = varinats
    return render(requset, 'voting.html', context)

def votes(requset):
    context = {'pagename':'title'}
    vote = Vote(title=random.randint(10, 99), description="asdasds", mode=1)
    context['votes'] = Vote.objects.all()
    return render(requset, 'pages/votes_create.html', context)
