from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == "GET":
        username = request.GET['name']
        location = request.GET['location']
        lang = request.GET['lang']
        check = request.GET['check']
        context = {'username': username, 'location': location, 'lang': lang, 'check': check}
    return render(request, 'show.html', context)