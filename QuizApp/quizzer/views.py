from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.template import loader

from .models import Question
# Create your views here.

counter = 0
correct = 0
incorrect = 0
score = 0
limit = 2

def index(request):
    
    global counter
    global correct
    global incorrect
    global score
    global limit

    template = loader.get_template("quizzer/index.html")
    
    # I want to make a change so that only one question is shown

    if request.method == 'POST':
        question = Question.objects.all()[counter]
        choice = request.POST.get ('choice '+str(counter + 1))
        # print ('Choice question ', counter, ': ')
        # print (choice)
        chosen = choice # This is redundant but I still keep it
        if question.correct_response == chosen:
            correct += 1
        else:
            incorrect += 1
        counter += 1
        if (counter == limit):
            score = correct
            context = {'incorrect': incorrect, 'correct': correct, 'score':score}
            return render(request, 'quizzer/results.html',  context)
        question = Question.objects.all()[counter]
        context = {'question': question}
        return HttpResponse(template.render(context, request))
    else:
        question = Question.objects.all()[counter]
        context = {'question': question}
        return HttpResponse(template.render(context, request))
