from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='home'),
    path("detail/<int:pk>/",views.Detail.as_view(),name="detail"),
    path("category/<str:name>/",views.categoryDetail,name = "categoryDetail"),
]
