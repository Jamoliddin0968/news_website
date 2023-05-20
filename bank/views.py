from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Exchange,Daily
from .serializers import ExchangeSerializer
from django.utils import timezone
from django.core.cache import cache


class Test(APIView):
    def get(self,request):
        data = get_all_data()
        return Response(data)
    

class ExchangeListAPIView(ListAPIView):
    def get_queryset(self):
        obj = Daily.objects.last()        
        return Exchange.objects.filter(daily_id=obj.id).select_related('bank').order_by('bank__name')

    def get(self,request,*args, **kwargs):
        data = cache.get('currency_data')
        if data:
            return Response(data)
            
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        

        data = self.get_serializer(queryset, many=True).data
        cache.set('currency_data', data, 60 * 3)
        
        return Response(data)
    serializer_class = ExchangeSerializer
    