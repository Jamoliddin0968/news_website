import requests
from bs4 import BeautifulSoup as bs
from .base import BaseBankClass

class Xalq(BaseBankClass):
    bank_name = 'Infinity bank'
    
    
    @classmethod
    def get_data(self):
        try:
            response = requests.get('https://xb.uz/api/v1/site/translations/uz/react')
            data = response.json()
            
            
            return {
                'success':True,
                'bank_name':self.bank_name,
                'olish':olish,
                'sotish':sotish
            }
        except:
            return {
                'success':False
            }
        
        # print(response.text)
        