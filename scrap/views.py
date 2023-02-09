from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from scrap.extractors.wwr import jobs_wwr
from scrap.extractors.idd import jobs_idd

import os
import json

def index(request):
    return render(request, 'index.html/')

def wwr_crap_view(request):
    ''' #### we work remotely 사이트 채용공고 스크랩 #### '''

    keyword = request.GET.get('keyword')
    if keyword is not None:
        result = jobs_wwr(keyword)
        return HttpResponse(json.dumps(result), content_type='application/json')

def idd_crap_view(request):
    ''' #### Indeed 사이트 채용공고 스크랩 #### '''
    keyword = request.GET.get('keyword')

    if keyword is not None:
        result = jobs_idd(keyword)
        export_excel(keyword, result) # 검색 결과 엑셀 출력

        return HttpResponse(json.dumps(result), content_type='application/json')

def export_excel(keyword, jobs):
    ''' #### Json형식 결과물 출력 #### '''
    directory = 'files/'

    if keyword is not None:
        create_folder(directory)    # 다운로드 폴더 생성 

        file = open(f'files/{keyword}.csv', 'w')
        file.write('Number,Postion,Company,Location,URL\n')
        for number, job in enumerate(jobs):
            file.write(f'{number+1},{job["position"]},{job["company"]},{job["location"]},{job["url"]}\n')
        file.close()

def create_folder(directory):
    ''' #### 폴더유무 확인 후 저장소 생성 #### '''
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def export_excel_view(request):
    keyword = request.GET.get('keyword')
    if keyword is not None:
        file = open(f'files/{keyword}.csv', 'w')
        file.write('Postion,Company,Location,URL\n')
        file.close()
        return HttpResponse(json.dumps({'keyword' : keyword}), content_type='application/json')
