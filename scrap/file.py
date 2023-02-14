import json
import os
from django.http import HttpResponse
from requests import request

def save_to_file(file_name, jobs):
    ''' #### Json형식 결과물 출력 #### '''
    directory = 'files/'

    create_folder(directory)    # 다운로드 폴더 생성 

    file = open(f'files/{file_name}.csv', 'w')
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