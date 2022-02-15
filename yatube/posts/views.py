from django.shortcuts import render
from django.http import HttpResponse
# Импортируем модель, чтобы обратиться к ней
from .models import Post

def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 
    

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