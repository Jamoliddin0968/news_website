from django.contrib import admin

# Register your models here.
from .models import Daily,Bank

admin.site.register((Daily,Bank))
