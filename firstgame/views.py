from django.shortcuts import render

def index(request):
    curget = str(request.GET)
    return render(request, 'index.html', {"getparam": curget})

