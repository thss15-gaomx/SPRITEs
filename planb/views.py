from django.shortcuts import render
from django.db.models import Q
from .models import Page
from .forms import UploadForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse
import json


def select(request, section_id):
    info = {'section': section_id}
    return render(request, "select.html", info)


def text(request, info_str):
    return render(request, "text.html")
    # if 'w' in info_str:
    #     index_1 = info_str.find('w')
    #     section_id = info_str[1:index_1]
    #     index_2 = info_str.find('h')
    #     section_w= info_str[index_1+1:index_2]
    #     section_h= info_str[index_2+1:]
    # else:
    #     section_id = info_str
    # if request.method == 'POST':
    #     width = request.POST.get('width')
    #     height = request.POST.get('height')
    #     block = create_block(width, height, "text", section_id)
    #     block.text_content = request.POST.get('content')
    #     block.font_size = request.POST.get('font-size')
    #     block.font_color = request.POST.get('font-color')
    #     block.background_color = request.POST.get('background-color')
    #     block.save()
    #     section = Section.objects.get(id=int(section_id))
    #     info = get_layout(section.page_id, block.id, section_id)
    #     try:
    #         return render(request, "layout.html", info)
    #     except:
    #         return render(request, "text.html", {'section': section_id, 'section_width': '1', 'section_height': '1'})
    # else:
    #     return render(request, "text.html", {'section': section_id, 'section_width': section_w, 'section_height': section_h})
    #


def page(request):
    pages = Page.objects.all()
    page_num = len(pages)
    return render(request, "page-b.html", {"pages": pages, "num": page_num})


def new_page(request):
    page = Page()
    page.header = 1
    page.sidebar = 1
    page.footer = 1
    page.section_num = 0
    page.save()
    try:
        return render(request, "layout-b.html", get_layout(page.id, -1, -1))
    except:
        return render(request, "page-b.html", {"pages": Page.objects.all(), "num": len(Page.objects.all())})


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
        return render(request, "layout-b.html", get_layout(pageId, -1, -1))
    else:
        return render(request, "layout-b.html", get_layout(pageId, -1, -1))


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
        return render(request, "layout-b.html", get_layout(page_id, -1, 0))
    elif 'w' in delete_info:
        index = delete_info.find('w')
        widget_id = delete_info[index+1:]
        page_id = delete_info[1:index]
        block = Block.objects.get(id=int(widget_id));
        section_id = block.section_id
        block.delete()
        return render(request, "layout-b.html", get_layout(page_id, -1, section_id))
    else:
        page_id = delete_info[1:]
        sections = Section.objects.filter(page_id=int(page_id))
        for section in sections:
            Block.objects.filter(section_id=int(section.id)).delete()
            section.delete()
        Page.objects.get(id=int(page_id)).delete()
        return render(request, "page-b.html", {"pages": Page.objects.all(), "num": len(Page.objects.all())})
    return render(request, "page-b.html", {"pages": Page.objects.all(), "num": len(Page.objects.all())})
