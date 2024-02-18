from django.db import models

# Create your models here.

class Question (models.Model):
    question_text = models.CharField (max_length = 1000)
    choice_1 = models.CharField (max_length = 500)
    choice_2 = models.CharField (max_length = 500)
    choice_3 = models.CharField (max_length = 500)
    choice_4 = models.CharField (max_length = 500)
    correct_response = models.CharField (max_length = 500)
    
    def __str__ (self):
        return self.question_text
    def getCorrectResponse (self):
        return correct_response
