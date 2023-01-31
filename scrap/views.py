from django.shortcuts import render
from django.http import HttpResponse
from scrap.extractors.wwr import wwr_jobs
from scrap.extractors.idd import idd_jobs

def index(request):
    return HttpResponse('Hello! This is Index Page')

def wwr_crap_view(request):
    result = wwr_jobs('python')

    return HttpResponse(result)

def idd_crap_view(request):
    result = idd_jobs('python')

    return HttpResponse(result)
