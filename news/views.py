from django.shortcuts import render, get_object_or_404

# https://htmlcodex.com/demo/?item=456
from .models import Post, Ads, Category
from django.utils.translation import gettext_lazy as _
from taggit.models import Tag

def index(request):
    ds = {}
    news = Post.objects.all()
    for cat in Category.objects.all():
        qs = cat.post_set.all().order_by("-id")[:3]
        ds[cat.name] = qs
    context = {
        "top_post": Post.objects.first(),
        "top_post_four": news[1:5],
        "cats":ds,
        'latest_news':news.last(),
        'latest_news_five':news[:5],
    }
    for i in context["cats"]["Sport"]:
        print(i)
        print("---------------------------------")
    return render(request, "index.html", context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    context = {
        "post": post,
    }
    return render(request, "single_page.html", context)


def regionDetail(request, pk):
    pass


def categoryDetail(request, name):
    category = get_object_or_404(Category, name=name)
    top_four_post = category.post_set.all()
    len_of_post = 5 if len(top_four_post) > 5 else len(top_four_post)
    context = {
        "top_post": category.post_set.first(),
        "top_post_four": top_four_post[1:len_of_post],
    }
    return render(request, "index.html", context)


def tagDetail(request, pk):
    pass


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
        


