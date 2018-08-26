from django.shortcuts import render


def select(request):
    return render(request, "select.html")


def settings(request):
    return render(request, "settings.html")


def text(request):
    if request.method == 'POST':
        width = request.POST.get('width')
        height = request.POST.get('height')
        content = request.POST.get('content')
        try:
            return render(request, "grid.html", {'width': width, 'height': height, 'content': content, 'type': "text"})
        except:
            return render(request, "text.html")
    else:
        return render(request, "text.html")


def grid(request):
    return render(request, "grid.html")