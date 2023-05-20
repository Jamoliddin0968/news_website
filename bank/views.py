from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Exchange,Daily
from .serializers import ExchangeSerializer
from .banks.master import get_all_data
from django.utils import timezone
class Test(APIView):
    def get(self,request):
        data = get_all_data()
        return Response(data)
    

class ExchangeListAPIView(ListAPIView):
    def get_queryset(self):
        curr = timezone.now().date()
        obj = Daily.objects.last()
        if not obj or obj.date.date() < curr:
            obj = Daily.objects.create()
            obj.generate_daily_data()
            
        return Exchange.objects.filter(daily_id=obj.id).order_by('bank_name')

        
    serializer_class = ExchangeSerializer
    
    