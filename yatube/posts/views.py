from django.shortcuts import render, get_object_or_404

from .models import Post, Group

POSTS_PER_PAGE = 10


def index(request):
    posts = (Post.objects.select_related('group', 'author').order_by
             ('-pub_date')[:POSTS_PER_PAGE])
    return render(request, 'posts/index.html', {'posts': posts})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related().order_by('-pub_date')[:POSTS_PER_PAGE]
    return render(request, 'posts/group_list.html', {'group': group,
                                                     'posts': posts})
