from django.shortcuts import render, get_object_or_404

# https://htmlcodex.com/demo/?item=456
from .models import Post, Ads


def index(request):
    context = {
        "top_post": Post.objects.first(),
        "top_post_four": Post.objects.all()[1:5],
    }
    return render(request, "index.html", context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    tags = post.tags.all()
    ads = Ads.objects.all()
    context = {
        "post": post,
        "tags": tags,
        "ads": ads,
    }
    return render(request, "single_page.html", context)

def regionDetail(request,pk):
    pass
def categoryDetail(request,pk):
    pass
def tagDetail(request,pk):
    pass