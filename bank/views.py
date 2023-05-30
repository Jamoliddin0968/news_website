import threading

from django.core.cache import cache
from django.shortcuts import render
from django.utils import timezone
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from bank.banks.master import get_all_data

from .models import Daily, Exchange
from .serializers import ExchangeSerializer


class Test(APIView):
    def get(self, request):
        thread = threading.Thread(target=get_all_data)
        thread.start()
        return Response({"ok": True})


class ExchangeListAPIView(APIView):

    def get(self, request):
        data = cache.get('currency_data')
        if data:
            return Response(data)

        obj = Daily.objects.filter(completed=True).last()
        queryset = Exchange.objects.filter(
            daily_id=obj.id).select_related('bank').order_by('bank__name')
        old_data = ExchangeSerializer(queryset, many=True).data
        data = {
            'last_date': obj.date,
            'data': old_data
        }
        cache.set('currency_data', data, 60 * 5)
        return Response(data)
