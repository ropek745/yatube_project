from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')
    

# Страница со списком групп
def groups_posts(request, slug):
    return HttpResponse(f'Информация о {slug}')


def groups_posts_list(request):
    return HTTPResponse('Список групп')