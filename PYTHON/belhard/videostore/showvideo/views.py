from django.shortcuts import render
from django.http import HttpResponse
from .models import Video

def hello(request):
    return HttpResponse("hello world")


def world(request):
    response = {"name":"Bogdan"}
    response["content"] = Video.objects.all()
    return render(request,"index.html", response)


# Create your views here.
