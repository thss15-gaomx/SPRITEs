from django.shortcuts import render
from django.db.models import Q
# from .models import Block, Text, Pic
# from .forms import UploadForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json

color_map = ["#B03060", "#FE9A76", "#FFD700", "#32CD32", "#016936", "#008080", "#0E6EB8", "#EE82EE", "#B413EC",
             "#FF1493", "#A52A2A", "#A0A0A0", "#000000"]


def select(request):
    return render(request, "select-b.html")


def text(request):
    return render(request, "text-b.html")


def pic(request):
    return render(request, "pic-b.html")


def grid(request):
    return render(request, "grid-b.html")
