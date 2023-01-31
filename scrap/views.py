from django.shortcuts import render
from django.http import HttpResponse
from scrap.extractors.wwr import jobs_wwr
from scrap.extractors.idd import jobs_idd

def index(request):
    return HttpResponse('Hello! This is Index Page')

def wwr_crap_view(request):
    result = jobs_wwr('python')

    return HttpResponse(result)

def idd_crap_view(request):
    result = jobs_idd('python')

    return HttpResponse(result)
