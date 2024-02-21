from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.template import loader

from .models import Question
# Create your views here.

def index(request):
    template = loader.get_template("quizzer/index.html")
    
    if request.method == 'POST':
        counter = 1
        questions=Question.objects.all()
        correct = 0
        incorrect = 0
        score = 0
        for q in questions:
            # Since, all answers are received in this post request, we dedicate a counter
            # to get choice for each question.
            choice = request.POST.get ('choice '+str(counter))
            print ('Choice question ', counter, ': ')
            print (choice)
            dict_ = vars(q) # This gives access to q
            chosen = dict_.get(choice)
            if q.correct_response == chosen:
                correct += 1
            else:
                incorrect += 1
            counter = counter + 1
        score = correct
        context = {'incorrect': incorrect, 'correct': correct, 'score':score}
        return render(request, 'quizzer/results.html',  context)

    else:
        questions = Question.objects.all()
        context = {'questions': questions}
        return HttpResponse(template.render(context, request))
