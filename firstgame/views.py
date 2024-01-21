from django.shortcuts import render
from django.conf import settings as cur_settings
from gameback.vk_common import checksign
from rest_framework.response import Response

def index(request):
    curget = dict(request.GET)
    pkey = cur_settings.VK_PRIVATE_KEY
    (checkresult, state) = checksign(pkey, curget)
    return render(request, 'index.html', {"getparam": state})

def updstate(request):
    curget = dict(request.GET)
    pkey = cur_settings.VK_PRIVATE_KEY
    curget['app_id'] = '51831674'
    curget['sign_keys'] = 'app_id,request_id,ts,user_id'
    (checkresult, state) = checksign(pkey, curget)
    serializer = ApiFullSerializer(fullreport.apistat, many=True)
    return Response({"fullreport":serializer.data})
