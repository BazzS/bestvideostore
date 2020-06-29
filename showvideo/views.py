from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Video, Comment

def hello(request):
    return HttpResponse("hello world")


def world(request):
    response = {"name":"Bogdan"}
    response["content"] = Video.objects.all()
    return render(request,"index.html", response)

def accept_comment(request, id):
    Comment.objects.create(text=request.GET['com'], comment_video_id=id)
    # print(id)
    # print(request.GET["com"])
    return redirect("main_page")


def one_video(request, id):
    response = {'video':Video.objects.get(id=id)}
    return render(request, "one_video.html", response)
