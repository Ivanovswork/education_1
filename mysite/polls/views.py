from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question, Choice
from django.db.models import Max



def index(request):
    list_of_last_question = Question.objects.order_by("-date_pub")[:5]
    context = {
        "list_of_last_question" : list_of_last_question
    }
    return render(request, 'polls/index.html/', context)


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {
        "question": question
    }
    return render(request, 'polls/detail.html/', context)


def result(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    choice = question.choices.order_by('-voice')[0]
    print(choice)
    context = {
        "question": question,
        "choice": choice,
    }
    return render(request, 'polls/result.html/', context)


def vote(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    choice.voice = choice.voice + 1
    choice.save()
    context = {
        "choice": choice
    }
    return render(request, 'polls/vote.html/', context)