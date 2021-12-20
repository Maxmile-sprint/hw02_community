from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Сreating a view-functions for receiving requests and generating responses.
# View-function returns HTML-code from templates.

def index(request):
    title = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    slug_list = Group.objects.values_list('slug', flat=True)[:]
    context = {
        'title': title,
        'posts': posts,
        'slug_list': slug_list
        }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    title = group.title
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title,
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)
