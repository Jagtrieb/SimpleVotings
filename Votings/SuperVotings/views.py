from django.shortcuts import render

def index(request):
    context = {}
    context['name'] = 'Egorka'
    return render(request, 'index.html', context)
