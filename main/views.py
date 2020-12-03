from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'main/sample.html')

def calc(request):
    context = {

    }
    template = 'main/calc.html'

    return render(request, template, context)


def instruction(request):
    table = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    row_size = 3
    col_size = 3
    context = {
        'table': table,
        'row_size': row_size,
        'col_size': col_size,
    }
    template = 'main/instruction.html'

    return render(request, template, context)


def about(request):
    context = {

    }

    template = 'main/about.html'

    return render(request, template, context)


def set_size(request):
    context = {

    }

    template = 'main/set_size.html'


    if request.method == 'GET':

        if request.GET.get("one_matr"):
            return HttpResponse('А рабитает'+'1')
        elif request.POST.get("two_matr"):  # You can use else in here too if there is only 2 submit types.
            return HttpResponse('А рабитает'+'2')

    return render(request, template, context)


