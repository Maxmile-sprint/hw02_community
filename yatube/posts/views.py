from django.shortcuts import render, get_object_or_404
from .models import Post, Group

POSTS_LIMIT = 10


# Сreating a view-functions for receiving requests and generating responses
# for main page and page with community posts.

def index(request):
    posts = (Post.objects.select_related("author").all()
             .order_by('-pub_date')[:POSTS_LIMIT])
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts_grp.order_by('-pub_date')[:POSTS_LIMIT]
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)
