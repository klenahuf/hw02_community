from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from . import constants as posts_c


def index(request):
    posts = (Post.objects.select_related('group', 'author').all()
             [:posts_c.NUM_POSTS_PER_PAGE])
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
