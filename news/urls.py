from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("detail/<int:pk>/",views.detail,name="detail"),
]
