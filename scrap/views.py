from django.shortcuts import render
from django.http import HttpResponse
from scrap.extractors.wwr import jobs_wwr
from scrap.extractors.idd import jobs_idd
from scrap.file import save_to_file

import os
import json

db = {}


def index(request):
    return render(request, 'index.html/')

def scrap_view(request):
    ''' #### 사이트 채용공고 스크랩 #### '''

    keyword = request.GET.get('keyword')
    jobs = {}
    if keyword != '':
        
        if keyword in db:
            jobs[keyword] = db[keyword]
        else:
            wwr = jobs_wwr(keyword)
            idd = jobs_idd(keyword)
            jobs[keyword] = wwr+idd
            db[keyword] = wwr+idd
        # save_to_file(keyword, jobs) # 검색 결과 엑셀 출력

    return HttpResponse(json.dumps(jobs[keyword]), content_type='application/json')