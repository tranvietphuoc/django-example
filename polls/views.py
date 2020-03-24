from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# Create your views here.
def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def result(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}"