from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from scrap.extractors.wwr import jobs_wwr
from scrap.extractors.idd import jobs_idd

import json

def index(request):
    return render(request, 'index.html/')

def wwr_crap_view(request):
    keyword = request.GET.get('keyword')
    if keyword is not None:
        result = jobs_wwr(keyword)
        return HttpResponse(json.dumps(result), content_type='application/json')

def idd_crap_view(request):
    keyword = request.GET.get('keyword')
    if keyword is not None:
        result = jobs_idd(keyword)
        return HttpResponse(json.dumps(result), content_type='application/json')
