from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.template import loader

from .models import Question
# Create your views here.

def index(request):
    template = loader.get_template("quizzer/index.html")
    questions = Question.objects.all()
    context = {'questions': questions}
    return HttpResponse(template.render(context, request))

def results (request, score):
    return HttpResponse ('Score :', str(score))

