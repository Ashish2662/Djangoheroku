from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello! world</h1>")