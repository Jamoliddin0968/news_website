from django.shortcuts import render
from bank.banks.master import get_all_data
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Exchange, Daily
from .serializers import ExchangeSerializer
from django.utils import timezone
from django.core.cache import cache


class Test(APIView):
    def get(self, request):
        data = get_all_data()
        return Response({"ok":True})


class ExchangeListAPIView(APIView):

    def get(self, request):
        data = cache.get('currency_data')
        if data:
            return Response(data)

        obj = Daily.objects.last()
        queryset = Exchange.objects.filter(
            daily_id=obj.id).select_related('bank').order_by('bank__name')
        old_data = ExchangeSerializer(queryset, many=True).data
        data = {
            'last_date': obj.date,
            'data': old_data
        }
        cache.set('currency_data', data, 60 * 3)
        return Response(data)
