import random

from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from SuperVotings.forms import RadioForm, AddSnippetForm
import random
from SuperVotings.models import Vote, Participant
def index(request):
    context = {}
    context['votes'] = Vote.objects.all()
    spisok=context['votes']
    if len(spisok) != 0:
        context['id'] = [spisok[random.randint(0, len(context['votes'])-1)], spisok[random.randint(0, len(context['votes'])-1)], spisok[random.randint(0, len(context['votes'])-1)], spisok[random.randint(0, len(context['votes'])-1)], spisok[random.randint(0, len(context['votes'])-1)], spisok[random.randint(0, len(context['votes'])-1)], spisok[random.randint(0, len(context['votes'])-1)], spisok[random.randint(0, len(context['votes'])-1)], spisok[random.randint(0, len(context['votes'])-1)]]
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
        find_votes = Vote.objects.filter(title=res)
    else:
        find_votes = Vote.objects.filter(title=res)
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
    context['participants'] = Participant.objects.filter(vote_id=id)
    if request.method == 'POST':
        participant_id = request.POST.get("radio")
        participant = Participant.objects.filter(id=participant_id)
        count=participant[0].count
        participant.update(count=(count+1))
        print(participant[0].count)
    return render(request, 'pages/vote.html', context)

def votes_create1(request):
    context={}
    if request.method == 'POST':
        if request.POST.get("title") != "" and request.POST.get("description") != "" and request.POST.get("1") != "" and request.POST.get("2") != "" and request.POST.get("3") != "":
            title = request.POST.get("title", "Голосование")
            description = request.POST.get("description", "Голосуйте")
            vote = Vote(title=title, description=description, mode=1)
            vote.save()
            id = vote.id
            for i in range(1, 4):
                name = request.POST.get(str(i))
                participant = Participant(name=name, vote_id=id)
                participant.save()
            context['participants'] = Participant.objects.filter(vote_id=id)
            context['votes'] = Vote.objects.all()
            messages.add_message(request, messages.SUCCESS, "Сниппет успешно добавлен")
            return redirect('vote_view', id=id)
        else:
            messages.add_message(request, messages.ERROR, "Некорректные данные в форме")
            return redirect('votes_add')
    return render(request, 'pages/votes_create.html')

def results(request, id: int):
    context = {'pagename': 'page not found'}
    vote = Vote.objects.filter(id=id)
    if len(vote) == 0:
        return render(request, "404.html")
    context["pagename"] = vote[0].title
    context["vote"] = vote[0]
    return render(request, 'pages/result.html', context)