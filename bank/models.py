from django.db import models
from .banks.master import get_all_data as generate_data

class Daily(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    
    def generate_daily_data(self):
        self.exchange_set.all().delete()
        generate_data(self)
        return True        
        

class Exchange(models.Model):
    daily = models.ForeignKey(Daily, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=63)
    buy=models.IntegerField()
    sell=models.IntegerField()
    
    
    