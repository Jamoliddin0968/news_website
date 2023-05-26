from django.db import models
# from bank.banks.master import get_all_data as generate_data

class Daily(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    # def generate_daily_data(self):
    #     self.exchange_set.all().delete()
    #     generate_data(self)
    #     return True        
        
class Bank(models.Model):
    name = models.CharField(max_length=63)
    slug = models.CharField(max_length=63)
    image = models.ImageField(upload_to='images/bank/',null=True)
    
    def __str__(self) -> str:
        return self.name
      
class Exchange(models.Model):
    daily = models.ForeignKey(Daily, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    buy=models.IntegerField()
    sell=models.IntegerField()