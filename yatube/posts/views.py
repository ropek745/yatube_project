from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'posts/index.html'
    return render (request, template)
    

# Страница со списком групп
def group_posts(request, slug):
    return HttpResponse(f'Информация о {slug}')


def group_posts_list(request):
    return HttpResponse('Тут будет список групп')