from django.shortcuts import render

from django.http import HttpResponse


def riya_ors(request):
    return HttpResponse('<h1>welcome to ors app</h1>')


def welcome(request):
    return render(request, 'welcome.html')


def signup(request):
    return render(request, 'registration.html')


def signin(request):
    return render(request, 'login.html')



