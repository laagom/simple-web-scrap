from django.shortcuts import render
from django.http import HttpResponse

from requests import get

def scrap_view(request):

    base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="

    search_word = "python"

    response = get(f"{base_url}{search_word}")

    print(response)

    return HttpResponse("Hello")
