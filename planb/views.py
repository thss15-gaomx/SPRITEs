from django.shortcuts import render
from django.db.models import Q
from .models import Page, Section, Block
from .forms import UploadForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse
import json


def get_layout(pageId, block_id, section_id):
    page = Page.objects.get(id=pageId)
    sections = Section.objects.filter(page_id=pageId)
    sectionList = []
    index = 0
    all = ''
    cur_section = 0
    for section in sections:
        index += 1
        columns = (section.style).split('-')
        sectionList.append({
            "num": len(columns),
            "columns": columns,
            "section": index,
            "blocks": Block.objects.filter(section_id=section.id)
        })
        print(Block.objects.filter(section_id=section.id))
        if int(section.id) == int(section_id):
            cur_section = index
        all += str(section.id) + ',' + str(len(columns)) + ',' + str(section.style) + ';'
    if all != "":
        all = all[:-1]
    if not section_id:
        cur_section = -1;
    info = {
        'pageId': pageId,
        'sectionNum': page.section_num,
        'sections': sectionList,
        'all': all,
        'block_id': block_id,
        'section_id': cur_section
    }
    return info


def select(request, section_id):
    info = {'section': section_id}
    return render(request, "select-b.html", info)


def text(request, info_str):
    index = info_str.find('c')
    section_id = info_str[1:index]
    column = info_str[index+1:]
    if request.method == 'POST':
        block = Block()
        block.content_type = "text"
        block.section_id = int(section_id)
        block.column = int(column)
        block.text_content = request.POST.get('content')
        block.font_size = request.POST.get('font-size')
        block.font_color = request.POST.get('font-color')
        block.save()
        section = Section.objects.get(id=int(section_id))
        info = get_layout(section.page_id, block.id, section_id)
        try:
            return render(request, "layout-b.html", info)
        except:
            return render(request, "text-b.html", {'section': info_str})
    else:
        return render(request, "text-b.html", {'section': info_str})


def pic(request, info_str):
    index = info_str.find('c')
    section_id = info_str[1:index]
    column = info_str[index+1:]
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_pic = request.FILES['upload_pic']
            if form.cleaned_data['name']:
                name = form.cleaned_data['name']
            else:
                name = upload_pic.name
            block = Block()
            block.content_type = "pic"
            block.section_id = int(section_id)
            block.column = int(column)
            block.name = name
            block.pic_content = upload_pic
            block.save()
            section = Section.objects.get(id=int(section_id))
            info = get_layout(section.page_id, block.id, section_id)
            try:
                return render(request, "layout-b.html", info)
            except:
                return render(request, "pic-b.html", {'section': info_str})
    else:
        return render(request, "pic-b.html", {'section': info_str})


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


def section(request, pageId):
    if request.method == 'POST':
        section = Section()
        section.page_id = pageId
        section.style = request.POST.get('style')
        section.name = request.POST.get('name')
        section.level = 1
        section.save()
        page = Page.objects.get(id=pageId)
        page.section_num += 1
        page.save()
        return render(request, "layout-b.html", get_layout(pageId, -1, section.id))
    else:
        return render(request, "layout-b.html", get_layout(pageId, -1, -1))


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
