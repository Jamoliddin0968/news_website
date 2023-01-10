from .models import Region , Category , Ads
from taggit.models import Tag
def getregion(request):
    tags = Tag.objects.all()
    ads = Ads.objects.all()
    return {
        "regions":Region.objects.all() ,
        "categories":Category.objects.all(),
        'tags':tags,
        'ads':ads,
    }