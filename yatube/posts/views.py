from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'posts/index.html'
    title = 'Проект "Yatube"'
    text = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'text': text,
    }
    return render (request, template, context)
    

# Страница со списком групп
def group_posts(request, slug):
    return HttpResponse(f'Информация о {slug}')


def group_posts_list(request):
    template = 'posts/group_list.html'
    title = 'Проект "Yatube"'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': text,
    }
    return render (request, template, context)