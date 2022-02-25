from django.http import HttpResponse
from django.shortcuts import render

from poll.models import Question


def index(request):
    # 자료 전체 가져오기
    question_list = Question.objects.all()
    return render(
        request,
        'poll/index.html',
        {'question_list': question_list}
    )
    # return HttpResponse("<h1>안녕~ Django!!</h1>")


def detail(request, pk):
    # 자료 1개 가져오기
    question = Question.objects.get(id=pk)
    return render(
        request,
        'poll/detail.html',
        {'question': question}
    )


def vote(request, pk):
    pass


def cart(request):
    cart = "계란"
    cartlist = ["계란", "두부", "커피"]
    return render(
        request,
        'poll/cart.html',
        {'cart': cart, 'cartlist': cartlist}
    )
