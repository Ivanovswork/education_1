from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello")


def detail(request, question_id):
    return HttpResponse(question_id)


def result(request, question_id):
    return HttpResponse(question_id)


def vote(request, question_id):
    return HttpResponse(question_id)