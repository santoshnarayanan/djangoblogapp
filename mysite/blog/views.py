from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Post


def post_list(request):
    post_list = Post.published.all()
    # Pagination with 3 Post per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page", 1)
    posts = paginator.page(page_number)
    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        status=Post.Status.PUBLISHED,
    )
    return render(request, "blog/post/detail.html", {"post": post})
