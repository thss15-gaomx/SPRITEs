from django.shortcuts import render
from django.db.models import Q
from .models import Block, Text, Pic
from .forms import UploadForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json

color_map = ["#B03060", "#FE9A76", "#FFD700", "#32CD32", "#016936", "#008080", "#0E6EB8", "#EE82EE", "#B413EC",
             "#FF1493", "#A52A2A", "#A0A0A0", "#000000"]


def create_block(width, height, type):
    new_block = Block()
    new_block.pos_x = 0
    new_block.pos_y = 0
    new_block.width = width
    new_block.height = height
    new_block.type = type
    new_block.save()
    new_block.color = color_map[new_block.id % 13]
    new_block.save()
    return new_block


def get_all_blocks():
    all = ""
    for block in Block.objects.all():
        all += str(block.id) + "," + str(block.pos_x) + "," + str(block.pos_y) + ";"
    if all != "":
        all = all[:-1]
    return all


def select(request):
    return render(request, "select.html")


def text(request):
    if request.method == 'POST':
        width = request.POST.get('width')
        height = request.POST.get('height')
        content = request.POST.get('content')
        font_size = request.POST.get('font-size')
        font_color = request.POST.get('font-color')
        new_text = Text()
        new_text.block = create_block(width, height, "text")
        new_text.content = content
        new_text.font_size = font_size
        new_text.font_color = font_color
        new_text.save()
        info = {
            'text': Text.objects.filter(~Q(id=new_text.id)),
            'pic': Pic.objects.all(),
            'all': get_all_blocks(),
            'object': new_text,
            'type': "text"
        }
        try:
            return render(request, "grid.html", info)
        except:
            return render(request, "text.html")
    else:
        return render(request, "text.html")


def pic(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_pic = request.FILES['upload_pic']
            width = form.cleaned_data['width']
            height = form.cleaned_data['height']
            if form.cleaned_data['name']:
                name = form.cleaned_data['name']
            else:
                name = upload_pic.name
            new_pic = Pic()
            new_pic.name = name
            new_pic.block = create_block(width, height, "pic")
            new_pic.content = upload_pic
            new_pic.save()
            info = {
                'pic': Pic.objects.filter(~Q(id=new_pic.id)),
                'text': Text.objects.all(),
                'all': get_all_blocks,
                'object': new_pic,
                'type': "pic"
            }
            try:
                return render(request, "grid.html", info)
            except:
                return render(request, "pic.html")
    else:
        return render(request, "pic.html")


def pic_text(request):
    return render(request, "pic-text.html")


def video(request):
    return render(request, "video.html")


def input(request):
    return render(request, "input.html")


def button(request):
    return render(request, "button.html")


def section(request):
    return render(request, "section.html")


def part(request):
    return render(request, "part.html")


def page(request):
    return render(request, "page.html")


@csrf_exempt
def grid(request):
    if request.method == 'POST':
        column = request.POST.get('x')
        row = request.POST.get('y')
        id = request.POST.get('id')
        object = Block.objects.get(id=id)
        object.pos_x = column
        object.pos_y = row
        object.save()
        return render(request, "grid.html")
    else:
        return render(request, "grid.html")


def layout(request):
    return render(request, "layout.html")
