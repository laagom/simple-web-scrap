from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import FileResponse
from scrap.extractors.wwr import jobs_wwr
from scrap.extractors.idd import jobs_idd
from scrap.file import save_to_file

import json

db = {}

def index(request):
    return render(request, 'home.html/')

def search_view(request):
    keyword = request.GET.get('keyword')
    return render(request, 'index.html', {'keyword' : keyword})

def scrap_view(request):
    ''' #### 사이트 채용공고 스크랩 #### '''
    keyword = request.GET.get('keyword')
    jobs = {}

    if keyword == None:
        return redirect("/")
    
    if keyword != '':
        
        # keyword가 가장 db에 저장되어 있으면(이전에 검색한 기록이 있으면)
        if keyword in db:
            jobs[keyword] = db[keyword]
            
        else:
            # db에 저장되어 있는 기록이 없으면 조회
            wwr = jobs_wwr(keyword)
            idd = jobs_idd(keyword)
            jobs[keyword] = wwr+idd
            db[keyword] = wwr+idd

    return HttpResponse(json.dumps(jobs[keyword]), content_type='application/json')

def export_view(request, **kwards):
    ''' #### 사이트 채용공고 스크랩 내용 파일 출력 #### '''
    keyword = request.GET.get('keyword')

    # keyword가 없이 접근
    if keyword == None or keyword == '': 
        return redirect("/")
    
    # keyword는 있지만 스크랩 없이 접근
    if keyword not in db: 
        return redirect("/")
    
    # 검색 결과 엑셀 출력
    save_to_file(keyword, db) 
    response = FileResponse(open(f'files/{keyword}.csv', 'rb'))

    return response