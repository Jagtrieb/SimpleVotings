import random

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from SuperVotings.forms import RadioForm

from SuperVotings.models import Vote


def index(request):
    context = {}
    context['name'] = 'user'



    return render(request, 'index.html', context)

def authorization(request):
    return render(request, 'authorization.html')

def restore_page(request):
    return render(request, 'restore_page.html')

def signup(request):
    return render(request, 'signup.html')

def voting_page(request):
    context = {}
    varinats = ['Putin', 'Trump', 'Xin Jin Pin']
    context['candidates'] = varinats
    return render(request, 'voting.html', context)

def votes_create(request):
    context = {'pagename':'title'}
    vote = Vote(title=random.randint(10, 99), description="Голосуйте", mode=1)
    vote.save()
    context['votes'] = Vote.objects.all()
    return render(request, 'pages/votes_create.html', context)

def votes_view(request: WSGIRequest, id: int):
    context = {'pagename':'page not found'}
    vote = Vote.objects.filter(id=id)
    if len(vote) == 0:
        return render(request, "404.html")
    context["pagename"] = vote[0].title
    context["vote"] = vote[0]
    return render(request, 'pages/vote.html', context)


