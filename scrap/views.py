from django.shortcuts import render
from django.http import HttpResponse
from scrap.extractors.wwr import extract_wwr_jobs

def index(request):
    return HttpResponse('Hello! This is Index Page')

def scrap_view(request):
    result = extract_wwr_jobs('python')

    return HttpResponse(result)
