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
        if request.GET.get("matr"):
            context['mode'] = request.GET.get('matr')

    return render(request, template, context)


def input_data(request):
    template = 'main/input_data.html'

    if request.method == 'GET':
        if request.GET.get("size_col_A") and request.GET.get("size_row_A"):
            row_size = int(request.GET.get("size_row_A"))
            col_size = int(request.GET.get("size_col_A"))
            table = [[i+(j*row_size) for i in range(row_size)] for j in range(col_size)]
    # if request.method == 'GET':

    context = {
        'table': table,
        'row': row_size,
        'col_size': col_size,
    }
    return render(request, template, context)

