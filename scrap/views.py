from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from scrap.extractors.wwr import jobs_wwr
from scrap.extractors.idd import jobs_idd

import os
import json

from scrap.file import save_to_file

def index(request):
    return render(request, 'index.html/')

def wwr_crap_view(request):
    ''' #### we work remotely 사이트 채용공고 스크랩 #### '''

    keyword = request.GET.get('keyword')
    if keyword is not None:
        result = jobs_wwr(keyword)
        save_to_file(keyword, result, 'We Work Remotely') # 검색 결과 엑셀 출력

        return HttpResponse(json.dumps(result), content_type='application/json')

def idd_crap_view(request):
    ''' #### Indeed 사이트 채용공고 스크랩 #### '''
    keyword = request.GET.get('keyword')

    if keyword is not None:
        result = jobs_idd(keyword)
        save_to_file(keyword, result, 'Indeed') # 검색 결과 엑셀 출력

        return HttpResponse(json.dumps(result), content_type='application/json')