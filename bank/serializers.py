from rest_framework.serializers import ModelSerializer

from .models import Exchange,Bank

class BankSerializer(ModelSerializer):
    class Meta:
        model = Bank
        exclude = ('id',)
class ExchangeSerializer(ModelSerializer):
    bank = BankSerializer()
    class Meta:
        model = Exchange
        fields = ("bank",'buy','sell')
        
