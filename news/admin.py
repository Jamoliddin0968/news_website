from django.contrib import admin

from .models import Post , Region , Category , Ads

admin.site.register((Post,Region,Category,Ads))
