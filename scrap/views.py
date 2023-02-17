from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import FileResponse
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

    if keyword == None:
        return redirect("/")
    
    if keyword != '':
        
        if keyword in db:
            jobs[keyword] = db[keyword]
        else:
            wwr = jobs_wwr(keyword)
            idd = jobs_idd(keyword)
            jobs[keyword] = wwr+idd
            db[keyword] = wwr+idd

    return HttpResponse(json.dumps(jobs[keyword]), content_type='application/json')

def export_view(request, **kwards):
    keyword = request.GET.get('keyword')

    if keyword == None or keyword == '':    # keyword가 없이 접근
        return redirect("/")
    if keyword not in db:   # keyword는 있지만 스크랩 없이 접근
        return redirect("/")
    
    save_to_file(keyword, db) # 검색 결과 엑셀 출력

    response = FileResponse(open(f'files/{keyword}.csv', 'rb'))

    return response