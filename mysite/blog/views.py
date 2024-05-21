from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Post


def post_list(request):
    post_list = Post.published.all()
    # Pagination with 3 Post per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page", 1)

    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        # if page_number is out of range get last page of results
        posts = paginator.page(paginator.num_pages)
        # if page is not an integer deliver the first page
    except PageNotAnInteger:
        posts = paginator.page(1)
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
