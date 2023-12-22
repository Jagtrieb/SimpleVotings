from django.shortcuts import render

def index(request):
    context = {}
    context['name'] = 'Egor'
    varinats = ['Putin', 'Trump', 'Xin Jin Pin']
    context['votings'] = varinats

    return render(request, 'index.html', context)

def authorization(request):
    return render(request, 'authorization.html')

def restore_page(requset):
    return render(requset, 'restore_page.html')
