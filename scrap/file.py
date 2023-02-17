import json
import os
from django.http import HttpResponse
from requests import request

def save_to_file(file_name, jobs):
    ''' #### Json형식 결과물 출력 #### '''
    directory = 'files/'

    create_folder(directory)    # 다운로드 폴더 생성 

    for job in jobs:

        file = open(f'files/{file_name}({job["site"]}).csv', 'w')
        file.write(f'{job["site"]}\n')
        file.write('Number,Postion,Company,Location,URL\n')
        for number, item in enumerate(job['list']):
            file.write(f'{number+1},{item["position"]},{item["company"]},{item["location"]},{item["url"]}\n')
        file.close()


def create_folder(directory):
    ''' #### 폴더유무 확인 후 저장소 생성 #### '''
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)