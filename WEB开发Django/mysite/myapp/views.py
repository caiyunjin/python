from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("hello world")


def user_list(request):
    return render(request, 'user_list.html')
