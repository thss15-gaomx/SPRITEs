from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def help1(request):
    return render(request, "help1.html")


def help2(request):
    return render(request, "help2.html")


def help3(request):
    return render(request, "help3.html")


def help4(request):
    if request.method == 'POST': # add the widget and input the position
        column = request.POST.get('column')
        row = request.POST.get('row')
        return render(request, "help4.html", {'column': int(column) - 1, 'row': int(row) - 1})
    else:
        return render(request, "help4.html", {'column': -1, 'row': -1})

def help5(request):
    return render(request, "help5.html")
