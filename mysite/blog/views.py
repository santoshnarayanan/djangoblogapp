from django.views.generic import ListView
from .forms import EmailPostForm
from django.shortcuts import get_object_or_404, render
from .models import Post

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"

def post_share(request,post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    # sent = False
    if request.method == "POST":
        # form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # form fields passed validation
            cd = form.cleaned_data
        else:
            form = EmailPostForm()
    return render(request, "blog/post/share.html", {"post": post,"form": form})

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
