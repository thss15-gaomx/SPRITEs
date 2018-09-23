from django.shortcuts import render
from django.db.models import Q
from .models import Block, Page, Section
from .forms import UploadForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse
import json
from .swipe_rec.test import swipe_convert

color_map = ["#B03060", "#FE9A76", "#FFD700", "#32CD32", "#016936", "#008080", "#0E6EB8", "#EE82EE", "#B413EC",
             "#FF1493", "#A52A2A", "#A0A0A0", "#000000"]


def create_block(width, height, type, section):
    new_block = Block()
    new_block.pos_x = 0
    new_block.pos_y = 0
    new_block.width = width
    new_block.height = height
    new_block.content_type = type
    new_block.section_id = int(section)
    new_block.save()
    return new_block


def get_all_blocks():
    all = ""
    for block in Block.objects.all():
        all += str(block.id) + "," + str(block.pos_x) + "," + str(block.pos_y) + ";"
    if all != "":
        all = all[:-1]
    return all


def get_layout(pageId, block_id, section_id):
    page = Page.objects.get(id=pageId)
    sections = Section.objects.filter(page_id=pageId)
    sectionList = []
    index = 0
    all = ''
    cur_section = 0
    for section in sections:
        index += 1
        sectionList.append({
            "width": range(0, section.width),
            "height": range(0, section.height),
            "section": index,
            "blocks": Block.objects.filter(section_id=section.id)
        })
        if int(section.id) == int(section_id):
            cur_section = index
        all += str(section.id) + ',' + str(section.width) + ',' + str(section.height) + ';'
    if all != "":
        all = all[:-1]
    if not section_id:
        cur_section = -1;
    info = {
        'pageId': pageId,
        'sectionNum': page.section_num,
        'section': sectionList,
        'all': all,
        'block_id': block_id,
        'section_id': cur_section
    }
    return info

@csrf_exempt
def playbox(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        key = key[:-1]
        keys = key.split(',')
        num_keys = []
        for item in keys:
            num_keys.append(int(item))
        result = 'loading'
        if num_keys:
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
        return render(request, "playbox.html")


def select(request, section_id):
    info = {'section': section_id}
    return render(request, "select.html", info)


def text(request, info_str):
    if 'w' in info_str:
        index_1 = info_str.find('w')
        section_id = info_str[1:index_1]
        index_2 = info_str.find('h')
        section_w= info_str[index_1+1:index_2]
        section_h= info_str[index_2+1:]
    else:
        section_id = info_str
    if request.method == 'POST':
        width = request.POST.get('width')
        height = request.POST.get('height')
        block = create_block(width, height, "text", section_id)
        block.text_content = request.POST.get('content')
        block.font_size = request.POST.get('font-size')
        block.font_color = request.POST.get('font-color')
        block.background_color = request.POST.get('background-color')
        block.save()
        section = Section.objects.get(id=int(section_id))
        info = get_layout(section.page_id, block.id, section_id)
        try:
            return render(request, "layout.html", info)
        except:
            return render(request, "text.html", {'section': section_id, 'section_width': '1', 'section_height': '1'})
    else:
        return render(request, "text.html", {'section': section_id, 'section_width': section_w, 'section_height': section_h})


def pic(request, info_str):
    if 'w' in info_str:
        index_1 = info_str.find('w')
        section_id = info_str[1:index_1]
        index_2 = info_str.find('h')
        section_w= info_str[index_1+1:index_2]
        section_h= info_str[index_2+1:]
    else:
        section_id = info_str
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
            block = create_block(width, height, "pic", section_id)
            block.name = name
            block.pic_content = upload_pic
            block.save()
            section = Section.objects.get(id=int(section_id))
            info = get_layout(section.page_id, block.id, section_id)
            try:
                return render(request, "layout.html", info)
            except:
                return render(request, "pic.html", {'section': section_id, 'section_width': section_w, 'section_height': section_h})
    else:
        return render(request, "pic.html", {'section': section_id, 'section_width': section_w, 'section_height': section_h})


def pic_text(request):
    return render(request, "pic-text.html")


def video(request):
    return render(request, "video.html")


def input(request):
    return render(request, "input.html")


def button(request):
    return render(request, "button.html")


def section(request, pageId):
    if request.method == 'POST':
        section = Section()
        section.page_id = pageId
        section.width = request.POST.get('width')
        section.height = request.POST.get('height')
        section.name = request.POST.get('name')
        section.save()
        page = Page.objects.get(id=pageId)
        page.section_num += 1
        page.save()
    return render(request, "layout.html", get_layout(pageId, -1, section.id))


def page(request):
    pages = Page.objects.all()
    page_num = len(pages)
    return render(request, "page.html", {"pages": pages, "num": page_num})


def new_page(request):
    page = Page()
    page.header = 1
    page.sidebar = 1
    page.footer = 1
    page.section_num = 0
    page.save()
    try:
        return render(request, "layout.html", get_layout(page.id, -1, -1))
    except:
        return render(request, "page.html", {"pages": Page.objects.all(), "num": len(Page.objects.all())})


@csrf_exempt
def layout(request, pageId):
    if request.method == 'POST':
        column = request.POST.get('x')
        row = request.POST.get('y')
        id = request.POST.get('id')
        object = Block.objects.get(id=id)
        object.pos_x = column
        object.pos_y = row
        object.save()
        return render(request, "layout.html", get_layout(pageId, -1, -1))
    else:
        return render(request, "layout.html", get_layout(pageId, -1, -1))


@csrf_exempt
def delete(request, delete_info):
    if 's' in delete_info:
        index = delete_info.find('s')
        section_id = delete_info[index+1:]
        page_id = delete_info[1:index]
        page = Page.objects.get(id=int(page_id))
        page.section_num -= 1
        page.save()
        Section.objects.get(id=int(section_id)).delete()
        Block.objects.filter(section_id=int(section_id)).delete()
        return render(request, "layout.html", get_layout(page_id, -1, 0))
    elif 'w' in delete_info:
        index = delete_info.find('w')
        widget_id = delete_info[index+1:]
        page_id = delete_info[1:index]
        block = Block.objects.get(id=int(widget_id));
        section_id = block.section_id
        block.delete()
        return render(request, "layout.html", get_layout(page_id, -1, section_id))
    else:
        page_id = delete_info[1:]
        print('hello')
        sections = Section.objects.filter(page_id=int(page_id))
        for section in sections:
            Block.objects.filter(section_id=int(section.id)).delete()
            section.delete()
        Page.objects.get(id=int(page_id)).delete()
        return render(request, "page.html", {"pages": Page.objects.all(), "num": len(Page.objects.all())})
    return render(request, "page.html", {"pages": Page.objects.all(), "num": len(Page.objects.all())})
