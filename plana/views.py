from django.shortcuts import render
from .models import Block, Text, Pic


color_map = ["#B03060", "#FE9A76", "#FFD700", "#32CD32", "#016936", "#008080", "#0E6EB8", "#EE82EE", "#B413EC",
             "#FF1493", "#A52A2A", "#A0A0A0", "#000000"]


def create_block(width, height):
    new_block = Block()
    new_block.pos_x = 0
    new_block.pos_y = 0
    new_block.width = width
    new_block.height = height
    new_block.save()
    new_block.color = color_map[new_block.id % 13]
    new_block.save()
    return new_block


def select(request):
    return render(request, "select.html")


def settings(request):
    return render(request, "settings.html")


def text(request):
    if request.method == 'POST':
        width = request.POST.get('width')
        height = request.POST.get('height')
        content = request.POST.get('content')
        font_size = request.POST.get('font-size')
        font_color = request.POST.get('font-color')
        new_text = Text()
        new_text.block = create_block(width, height)
        block_color = new_text.block.color
        new_text.content = content
        new_text.font_size = font_size
        new_text.font_color = font_color
        new_text.save()
        info = {
            'width': width,
            'height': height,
            'content': content,
            'font_size': font_size,
            'font_color': font_color,
            'block_color': block_color,
            'type': "text"
        }
        try:
            return render(request, "grid.html", info)
        except:
            return render(request, "text.html")
    else:
        return render(request, "text.html")


def grid(request):
    return render(request, "grid.html")