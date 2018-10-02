from django.shortcuts import render
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse
import json
from .swipe_rec.test import swipe_convert

color_map = ["#B03060", "#FE9A76", "#FFD700", "#32CD32", "#016936", "#008080", "#0E6EB8", "#EE82EE", "#B413EC",
             "#FF1493", "#A52A2A", "#A0A0A0", "#000000"]


def playbox(request):
    return render(request, "playbox.html")


def grid(request):
    return render(request, "grid-b.html")


@csrf_exempt
def swipe(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        key = key[:-1]
        keys = key.split(',')
        num_keys = []
        for item in keys:
            num_keys.append(int(item))
        result = 'loading'
        if num_keys:
            # get the gesture of the input
            swipe = swipe_convert(num_keys)
            if swipe == 1:
                result = 'both'
            elif swipe == 2:
                result = 'right'
            elif swipe == 3:
                result = 'left'
        return_json = {'result': result}
        return HttpResponse(json.dumps(return_json), content_type='application/json')
    else:
        return render(request, "swipe.html")
