from django.shortcuts import render
from django.conf import settings as cur_settings
from gameback.vk_common import checksign

def index(request):
    curget = dict(request.GET)
    pkey = cur_settings.VK_PRIVATE_KEY
    (checkresult, state) = checksign(pkey, curget)
    return render(request, 'index.html', {"getparam": state})

