from django.shortcuts import render
# import os

def index(request):
    # template = 'posts/index.html'
    title = "Это главная страница проекта Yatube"
    context = {
        # В словарь можно передать переменную
        'title': title,
    }
    return render(request, 'posts/index.html', context)
    # return render(request, 'posts/index.html')


def group_posts(request, slug):
    title = "Здесь будет информация о группах проекта Yatube"
    context = {
        # В словарь можно передать переменную
        'title': title,
    }
    # template = 'posts/group_list.html'
    return render(request, 'posts/group_list.html', context)
