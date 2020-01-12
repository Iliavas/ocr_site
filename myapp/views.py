from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import *
from .models import *
from django.views.generic import CreateView
from django.urls import reverse
import requests
import json
import os
import shutil
folder = 'media/pic_folder'
class HomePageView(View):
    def post(self, request):
        return HttpResponse('hello world')

def ocr_space_file(filetext, overlay=True, api_key='helloworld', language='eng'):
    payload = {'isOverlayRequired': overlay,
                   'apikey': api_key,
                   'language': language,
                   }
    r = requests.post('https://api.ocr.space/parse/image',
                          files={'res.png': filetext},
                          data=payload,
                          )
    return decode(json.loads(r.content))


def decode(sl):
    print(sl)
    if isinstance(sl, str):
        print('включи впн')
        return 'на сервере неполадки'
    try:
        lines = sl['ParsedResults'][0]['TextOverlay']['Lines']
    except:
        print('текст не найден')
        return 'we have no found any text'
    result = ''
    for i in lines:
        result += i['LineText'] + '\n'
    return result


def Succes(request):
    res = ''
    for file in os.listdir(folder):
        try:
            print(file)
            with open(folder+'/'+file, 'rb') as f:
                res = ocr_space_file(f)
        except:
            pass
    for file in os.listdir(folder):
        try:
            the_file = os.path.join(folder, file)
            if os.path.isfile(the_file):
                os.unlink(the_file)
            shutil.rmtree(the_file)
        except:
            pass
    print(res)
    return render(request, 'myapp/succes.html', context={'res': res})

class CreatePostView(CreateView):
    template_name = 'myapp/post.html'
    form_class = ImageUploadForm
    model = Im
    def get_success_url(self):
        return reverse('succes')