from django.urls import path

from . import views

app_name = 'quizzer'

urlpatterns = [
    path("", views.index, name="index"),
]
