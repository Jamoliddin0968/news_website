from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from datetime import datetime

def post_image_rename(instance, filename):
    ext = filename.split('.')[-1]
    name = str(datetime.now()).replace("-","").replace(":","").replace(" ","")
    filename = "%s.%s" % (name, ext)
    return f"post/{filename}"

def ad_image_rename(instance, filename):
    ext = filename.split('.')[-1]
    name = str(datetime.now()).replace("-","").replace(":","").replace(" ","")
    filename = "%s.%s" % (name, ext)
    return f"ads/{filename}"

class Ads(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=255)
    img = models.ImageField(upload_to=ad_image_rename)
    is_active = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = _("Ad")
        verbose_name_plural = _("Ads")
        
        
    
class Region(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")
        
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    img = models.ImageField(upload_to = post_image_rename)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    hit_count = models.PositiveIntegerField(default=0)
    tags = TaggableManager()
    
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse("_detail", kwargs={"pk": self.pk})
        pass
