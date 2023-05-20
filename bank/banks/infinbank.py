import requests
from bs4 import BeautifulSoup as bs
from .base import BaseBankClass


class InfinBank(BaseBankClass):
    bank_name = 'Infin bank'

    @classmethod
    def get_data(self):
        try:
            response = requests.get(
                'https://www.infinbank.com/uz/private/exchange-rates/')
            content = bs(response.text, 'html.parser')
            table = content.find('div', {'class': 'rates-table'}).find(
                'tbody').find_all('tr', {'class': 'rates-row--bg'})[:2]
            olish = table[0].find_all('td')[2].text.replace(' ', '')
            sotish = table[1].find_all('td')[1].text.replace(' ', '')
            
            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': float(olish),
                'sotish': float(sotish)
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class TuronBank(BaseBankClass):
    bank_name = 'Turon bank'

    @classmethod
    def get_data(self):
        try:
            response = requests.get('https://turonbank.uz/oz/')
            content = bs(response.text, 'html.parser')
            table = content.find(
                'table', {'class': 'currency__rate_table'}).find_all('tr')
            olish = table[1].find_all('td')[0].text
            sotish = table[2].find_all('td')[0].text

            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': olish,
                'sotish': sotish
            }
        except:
            return {
                'success': False
            }


class HamkorBank(BaseBankClass):
    bank_name = 'Hamkor bank'

    @classmethod
    def get_data(self):
        try:
            response = requests.get('https://hamkorbank.uz/uz/exchange-rate/')
            content = bs(response.text, 'html.parser')
            table = content.find('div', {'class': 'exchangeRates__content--wraps-content'}).find_all(
                'ul', {'class': "body"})[0].find_all('li')

            olish = table[3].text
            sotish = table[4].text

            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': olish,
                'sotish': sotish
            }
        except:
            return {
                'success': False
            }


class AgroBank(BaseBankClass):
    bank_name = 'Agro bank'

    @classmethod
    def get_data(self):
        try:
            params = {
                'action': 'pages',
                'code': 'uz/person/exchange_rates',
            }

            response = requests.get(
                'https://agrobank.uz/api/v1/', params=params)
            data = response.json()

            ex_data = data.get('data').get('sections')[
                0]['blocks'][2].get('content').get('items')[0]

            olish = ex_data.get('buy')
            sotish = ex_data.get('sale')

            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': olish,
                'sotish': sotish
            }
        except:
            return {
                'success': False
            }


class IpakYuliBank(BaseBankClass):
    bank_name = "Ipak yo'li bank"

    @classmethod
    def get_data(self):
        try:

            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
                'Connection': 'keep-alive',
                # 'Content-Length': '0',
                'Origin': 'https://ipakyulibank.uz',
                'Referer': 'https://ipakyulibank.uz/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42',
                'X-AppKey': 'blablakey',
                'X-AppLang': 'uz',
                'X-AppRef': '/physical',
                'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            response = requests.post(
                'https://ipakyulibank.uz:8888/webapi/default/get-other-contents', headers=headers)
            data = response.json()

            ex_data = data.get('data').get('exchange_rates_list').get('USD')

            olish = int(ex_data.get('buy'))//100
            sotish = int(ex_data.get('sale'))//100

            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': olish,
                'sotish': sotish
            }
        except:
            return {
                'success': False
            }


class MikroKreditBank(BaseBankClass):
    bank_name = 'Mikrokredit bank'

    @classmethod
    def get_data(self):
        try:
            response = requests.get('https://mkbank.uz/uz/index.php')
            content = bs(response.text, 'html.parser')
            ex_data = content.find('table', {'class': "exchange__table"}).find_all('tr')[
                1].find_all('td')
            olish = ex_data[1].text
            sotish = ex_data[2].text

            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': olish,
                'sotish': sotish
            }
        except:
            return {
                'success': False
            }


class SQBank(BaseBankClass):
    bank_name = 'Sanoat qurilish bank'

    @staticmethod
    def get_item_by_code(items, code):
        for item in items:
            if item['code'] == code:
                return item
        return None

    @classmethod
    def get_data(self):
        try:
            response = requests.get('https://sqb.uz/api/site-kurs-api/')
            data = response.json()

            data = data.get('data').get('offline')
            ex_data = self.get_item_by_code(data, 'USD')

            olish = ex_data.get('buy')//100
            sotish = ex_data.get('sell')//100

            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': olish,
                'sotish': sotish
            }
        except:
            return {
                'success': False
            }


class OFBank(BaseBankClass):
    bank_name = 'Orient Finans bank'

    @classmethod
    def get_data(self):
        try:
            response = requests.get('https://ofb.uz/uz/')
            content = bs(response.text, 'html.parser')
            ex_data = content.find_all('div', {'class': "rates__item"})[0].find_all(
                'div', {'class': 'rates__box rates__box--down currency'})
            olish = ex_data[1].text.strip('\n ')
            sotish = ex_data[0].text.strip('\n ')

            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': float(olish),
                'sotish': float(sotish)
            }
        except:
            return {
                'success': False
            }


class TrustBank(BaseBankClass):
    bank_name = 'Transbank'

    @classmethod
    def get_data(self):
        try:
            response = requests.get('https://trustbank.uz/uz/')
            content = bs(response.text, 'html.parser')

            ex_data = content.find(
                'table', {'class': "rate__table"}).find_all('span')[:2]
            olish = ex_data[0].text
            sotish = ex_data[1].text

            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': olish,
                'sotish': sotish
            }
        except:
            return {
                'success': False
            }


class ZiraatBank(BaseBankClass):
    bank_name = 'Ziraat bank'

    @staticmethod
    def get_item_by_code(items, code):
        for item in items:
            if item['name'] == code:
                return item
        return None

    @classmethod
    def get_data(self):
        try:
            response = requests.get('https://www.ziraatbank.uz/tr/GetCurrency')
            data = response.json()

            ex_data = self.get_item_by_code(data, 'USD')
            olish = ex_data.get('value')
            sotish = ex_data.get('oldValue')

            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': olish,
                'sotish': sotish
            }
        except:
            return {
                'success': False
            }


class KapitalBank(BaseBankClass):
    bank_name = 'Kapitalbank'

    @classmethod
    def get_data(self):
        try:
            response = requests.get(
                'https://www.kapitalbank.uz/uz/welcome.php')
            content = bs(response.text, 'html.parser')
            ex_data = content.find(
                'div', {'class': "item item-usd"}).find_all('span', {'class': 'item-value'})
            olish = ex_data[0].text.strip('\n ')
            sotish = ex_data[1].text.strip('\n ')

            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': olish,
                'sotish': sotish
            }
        except:
            return {
                'success': False
            }


class UniversalBank(BaseBankClass):
    bank_name = 'Universalbank'

    @classmethod
    def get_data(self):
        try:
            response = requests.get('https://universalbank.uz/private')
            content = bs(response.text, 'html.parser')
            ex_data = content.find('tr', {'class': "kurs"}).find_all('td')
            olish = ex_data[2].text
            sotish = ex_data[3].text

            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': olish,
                'sotish': sotish
            }
        except:
            return {
                'success': False
            }


class AsakaBank(BaseBankClass):
    bank_name = 'Asaka bank'

    @classmethod
    def get_data(self):
        try:
            params = {
                'type': 'asaka',
                'currency_type': 'individual',
                'page_size': '1',
            }
            response = requests.get(
                'https://back.asakabank.uz/1/currency/', params=params)
            data = response.json()
            ex_data = data.get('results')[0]

            olish = int(ex_data.get('buy'))//100
            sotish = int(ex_data.get('sell'))//100

            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': olish,
                'sotish': sotish
            }
        except:
            return {
                'success': False
            }


class IpotekaBank(BaseBankClass):
    bank_name = 'Ipoteka bank'

    @classmethod
    def get_data(self):
        try:
            data = {
                'iblockId': '8',
                'iblockType': 'astatroth_currency_iblock_type',
            }

            response = requests.post(
                'https://www.ipotekabank.uz/uz/ajax-handler.converter.php', data=data)
            data = response.json()

            ex_data = data.get('rates').get('USD')
            olish = ex_data.get('BUY')
            sotish = ex_data.get('SELL')

            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': olish,
                'sotish': sotish
            }
        except:
            return {
                'success': False
            }

class GarantBank(BaseBankClass):
    bank_name = 'Garantbank'

    @classmethod
    def get_data(self):
        try:
            response = requests.get('https://garantbank.uz/yz/')
            content = bs(response.text, 'html.parser')
            trs = content.find('table', {'class': "b-rates__table table-rate dtable"}).find_all('tr')
            olish = trs[2].find_all('td')[1].text
            
            sotish = trs[3].find_all('td')[1].text

            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': float(olish.replace(',', '.')),
                'sotish': float(sotish.replace(',', '.'))
            }
        except:
            return {
                'success': False
            }

class AABBank(BaseBankClass):
    bank_name = 'ASIA ALLIANCE BANK'

    @classmethod
    def get_data(self):
        try:
            response = requests.get('https://aab.uz/uz/')
            content = bs(response.text, 'html.parser')
            ex_data = content.find('div', {'class': "main-tabs__content active",'data-tabs-target':'exchange-01'}).find_all('tr')[1].find_all('td')
            olish = ex_data[1].text
            sotish = ex_data[2].text

            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': olish,
                'sotish': sotish
            }
        except:
            return {
                'success': False
            }


class AloqaBank(BaseBankClass):
    bank_name = 'Aloqabank'

    @classmethod
    def get_data(self):
        try:
            response = requests.get('https://aloqabank.uz/uz/index.php')
            content = bs(response.text, 'html.parser')
            ex_data = content.find('div', {'class': "exchange__group active",'data-tabs-target':'tab1'}).find_all('tr')[1].find_all('span')
            olish = ex_data[0].text
            sotish = ex_data[1].text

            return {
                'success': True,
                'bank_name': self.bank_name,
                'olish': olish,
                'sotish': sotish
            }
        except:
            return {
                'success': False
            }