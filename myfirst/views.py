from django.http import HttpResponse
from django.shortcuts import render
from random import randint
from datetime import datetime

def first_page(request):
    # return HttpResponse('<h1>Hello Django!</h1>') - можно так

    return render(request, './index.html')

def time_page(request):
    return render(request, './time_page.html', {
        'cur_time': str(datetime.now())
    })

def rand_num_page(request):
    return render(request, './rand_num.html', {
        'num': randint(1, 100)
    })