from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'allapp/index1.html')


def test(request):
    return HttpResponse("<h1>Это мой test</h1>")


def data(request):
    return HttpResponse("<h1>Это мой data</h1>")
