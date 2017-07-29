from django.shortcuts import render, redirect
from App.models import *


def index(request):
    # create nodes
    test_user = User()
    test_user.save()

    test_question = Question(title="Test Question")
    test_question.save()

    test_option1 = Option(title="Test Option 1")
    test_option1.save()

    test_option2 = Option(title="Test Option 2")
    test_option2.save()

    # create_relations
    test_option1.question.connect(test_question)
    test_option2.question.connect(test_question)
    test_user.answers.connect(test_option2)

    return render(request, 'index.html', {'users': User.nodes.all(), 'options': Option.nodes.all(), 'questions': Question.nodes.all()})
