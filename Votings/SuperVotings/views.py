from django.shortcuts import render, redirect
from django.contrib import messages


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
    cands = ['Putin', 'Trump', 'Xin Jin Pin']
    context['candidates'] = cands
    if requset.method == 'POST':
        variants = requset.POST.getlist('variants')
        #messages.success(requset, 'You have voted successfully!')
        print(variants)
        return redirect('index')

    return render(requset, 'voting.html', context)
