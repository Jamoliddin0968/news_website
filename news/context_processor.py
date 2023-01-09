from .models import Region , Category

def getregion(request):
    return {"regions":Region.objects.all() , "categories":Category.objects.all()}