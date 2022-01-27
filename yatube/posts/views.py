from django.shortcuts import render, get_object_or_404

from .models import Post, Group
# import os


def index(request):
    # template = 'posts/index.html'
    # title = "Это главная страница проекта Yatube"
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        # В словарь можно передать переменную
        # 'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)
    # return render(request, 'posts/index.html')


def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе,
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    # title = "Здесь будет информация о группах проекта Yatube"
    # context = {
    #     # В словарь можно передать переменную
    #     'title': title,
    # }
    # template = 'posts/group_list.html'
    return render(request, 'posts/group_list.html', context)
