import random

from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from SuperVotings.forms import RadioForm, AddSnippetForm

from SuperVotings.models import Vote
def index(request):
    context = {}
    context['votes'] = Vote.objects.all()

    return render(request, 'index.html', context)

def authorization(request):
    return render(request, 'authorization.html')

def restore_page(request):
    return render(request, 'restore_page.html')

def signup(request):
    return render(request, 'signup.html')

def s(request):
    context = {}
    res = request.POST.get("search", "")
    print("aboba")
    print(res)
    if res:
        find_votes=Vote.objects.filter(title=res)
    else:
        find_votes=Vote.objects.filter(title=res)
    context['votes'] = find_votes
    return render(request, 'pages/votes.html', context)

def voting_page(request):
    context = {}
    varinats = ['Putin', 'Trump', 'Xin Jin Pin']
    context['candidates'] = varinats
    return render(request, 'voting.html', context)

def votes(request):
    context = {}
    context['votes'] = Vote.objects.all()
    return render(request, 'pages/votes.html', context)

def votes_view(request: WSGIRequest, id: int):
    context = {'pagename':'page not found'}
    vote = Vote.objects.filter(id=id)
    if len(vote) == 0:
        return render(request, "404.html")
    context["pagename"] = vote[0].title
    context["vote"] = vote[0]
    return render(request, 'pages/vote.html', context)

def votes_create1(request):
    context={}
    if request.method == 'POST':
        if request.POST.get("title") != "" or request.POST.get("description") != "":
            title = request.POST.get("title", "Голосование")
            description = request.POST.get("description", "Голосуйте")
            vote = Vote(title=title, description=description, mode=1)
            vote.save()
            id = vote.id
            context['votes'] = Vote.objects.all()
            messages.add_message(request, messages.SUCCESS, "Сниппет успешно добавлен")
            return redirect('vote_view', id=id)
        else:
            messages.add_message(request, messages.ERROR, "Некорректные данные в форме")
            return redirect('votes_add')
    return render(request, 'pages/votes_create.html')


