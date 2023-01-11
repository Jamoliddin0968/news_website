from django.shortcuts import render, get_object_or_404

# https://htmlcodex.com/demo/?item=456
from .models import Post, Ads, Category
from django.utils.translation import gettext_lazy as _
from hitcount.views import HitCountDetailView
from hitcount.models import HitCount

def index(request):
    ds = {}
    news = Post.objects.all()
    for cat in Category.objects.all():
        qs = cat.post_set.all().order_by("-id")[:3]
        ds[cat.name] = qs
    popular_posts = news.all().order_by("hit_count")[:6]
    context = {
        "top_post": Post.objects.first(),
        "top_post_four": news[1:5],
        "cats":ds,
        'latest_news':news.last(),
        'latest_news_five':news[:5],
        "popular_news_five":popular_posts[1:5],
        'popular_news':popular_posts.first(),
    }
    return render(request, "index.html", context)


# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
    
#     context = {
#         "post": post,
#     }
#     return render(request, "single_page.html", context)


def regionDetail(request, pk):
    pass


def categoryDetail(request, name):
    category = get_object_or_404(Category, name=name)
    news = category.post_set.all()
    popular_posts = news.all().order_by("hit_count")[:6]
    context = {
        "top_post": news.first(),
        "top_post_four": news[1:5],
        'latest_news':news.last(),
        'latest_news_five':news[:5],
        "popular_news_five":popular_posts[1:5],
        'popular_news':popular_posts.first(),
    }
    return render(request, "index.html", context)


def tagDetail(request, pk):
    pass

# ko'rishlar soni

class Detail(HitCountDetailView):
    model = Post       
    count_hit = True
    template_name = "single_page.html"
    context_object_name = "post"

# generate fake data
from django.contrib.auth.models import User
from faker import Faker
fake = Faker()
def generate(cnt):
    for i in range(cnt):
        pk = fake.random_number(100)%8+1
        category = Category.objects.get(id = pk)
        title = fake.text()
        body = "".join(fake.texts())
        img = "post/20230109190403.467634.jpg"
        author = User.objects.first()
        tags = [1,2]
        a = Post(category = category,title=title,body=body,img=img,author=author,tags=tags)
        a.save()
        print(i)
        


