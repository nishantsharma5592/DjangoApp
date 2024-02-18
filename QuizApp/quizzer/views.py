from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.template import loader

from .models import Question
# Create your views here.

def index(request):
    template = loader.get_template("quizzer/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def show_next(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "quizzer/show_next.html", {"question": question})

def results (request):
    return HttpResponse ('Score :0')

