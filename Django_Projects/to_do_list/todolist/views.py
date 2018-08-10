from django.shortcuts import render

# Create your views here.


def home(request):
    context = {'content_post': request.POST, }
    # return render(request, "todolist/home.html", {'abc': str(request.POST)})
    # return render(request, "todolist/home.html", context.todo_add)
    return render(request, "todolist/home.html", context)


def aboutPage(request):
    return render(request, "todolist/about.html")


def edit(request):
    return render(request, "todolist/edit.html")
