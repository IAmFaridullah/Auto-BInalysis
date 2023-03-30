from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def train_model(request):
    print('anything')
    return HttpResponse('done')