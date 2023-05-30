import json

import requests
from bs4 import BeautifulSoup as bs

from .base import BaseBankClass


class InfinBank(BaseBankClass):

    bank_name = 'Infin bank'
    bank_slug = 'infinbank'

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
                'bank_slug': self.bank_slug,
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
    bank_slug = 'turonbank'

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
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class HamkorBank(BaseBankClass):
    bank_name = 'Hamkor bank'
    bank_slug = 'hamkorbank'

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
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class AgroBank(BaseBankClass):
    bank_name = 'Agro bank'
    bank_slug = 'agrobank'

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
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class IpakYuliBank(BaseBankClass):
    bank_name = "Ipak yo'li bank"
    bank_slug = 'ipakyolibank'

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
            ex_data = data['data']['exchange_rates_list']["USD"]

            olish = int(ex_data.get('buy'))//100
            sotish = int(ex_data.get('sale'))//100

            return {
                'success': True,
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class MikroKreditBank(BaseBankClass):
    bank_name = 'Mikrokredit bank'
    bank_slug = 'mikrokreditbank'

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
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class OFBank(BaseBankClass):
    bank_name = 'Orient Finans bank'
    bank_slug = 'ofbbank'

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
                'bank_slug': self.bank_slug,
                'olish': float(olish),
                'sotish': float(sotish)
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class TrustBank(BaseBankClass):
    bank_name = 'Trastbank'
    bank_slug = 'trastbank'

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
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class ZiraatBank(BaseBankClass):
    bank_name = 'Ziraat bank'
    bank_slug = 'ziraatbank'

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
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class KapitalBank(BaseBankClass):
    bank_name = 'Kapitalbank'
    bank_slug = 'kapitalbank'

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
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class UniversalBank(BaseBankClass):
    bank_name = 'Universalbank'
    bank_slug = 'universalbank'

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
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class AABBank(BaseBankClass):
    bank_name = 'Asia allianse bank'
    bank_slug = 'aabbank'

    @classmethod
    def get_data(self):
        try:
            response = requests.get('https://aab.uz/uz/')
            content = bs(response.text, 'html.parser')
            ex_data = content.find('div', {'class': "main-tabs__content active",
                                   'data-tabs-target': 'exchange-01'}).find_all('tr')[1].find_all('td')
            olish = ex_data[1].text
            sotish = ex_data[2].text

            return {
                'success': True,
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class MadadInvestBank(BaseBankClass):
    bank_name = 'Madad invest bank'
    bank_slug = 'madadinvestbank'

    @classmethod
    def get_data(self):
        try:
            response = requests.get('https://madadinvestbank.uz/currency')
            content = bs(response.text, 'html.parser')
            ex_data = content.find_all('tbody')[0].find_all('tr')[
                0].find_all('td')
            olish = float(ex_data[2].text.replace(' ', ''))
            sotish = float(ex_data[3].text.replace(' ', ''))

            return {
                'success': True,
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class GarantBank(BaseBankClass):
    bank_name = 'Garantbank'
    bank_slug = 'garantbank'

    @staticmethod
    def _get_item_by_code(items, code):
        for item in items:
            if item['Ccy'] == code:
                return item
        return None

    @classmethod
    def get_data(self):
        try:
            requests.packages.urllib3.disable_warnings()
            response = requests.get(
                'https://garantbank.uz/ru/exchange-rates/', verify=False)
            content = bs(response.text, 'html.parser')
            spans = content.find_all('tr')[2].find_all('span')[2:4]
            olish = spans[0].text

            sotish = spans[1].text
            return {
                'success': True,
                'bank_slug': self.bank_slug,
                'olish': float(olish.replace(',', '.')),
                'sotish': float(sotish.replace(',', '.'))
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False,
                'm': e.args
            }


class AloqaBank(BaseBankClass):
    bank_name = 'Aloqabank'
    bank_slug = 'aloqbank'

    @classmethod
    def get_data(self):
        try:
            response = requests.get('https://aloqabank.uz/uz/index.php')
            content = bs(response.text, 'html.parser')
            ex_data = content.find('div', {'class': "exchange__group active",
                                   'data-tabs-target': 'tab1'}).find_all('tr')[1].find_all('span')
            olish = ex_data[0].text
            sotish = ex_data[1].text

            return {
                'success': True,
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }
# #########################################################################################
# jsonli data


class AsakaBank(BaseBankClass):
    bank_name = 'Asaka bank'
    bank_slug = 'asakabank'

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
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class IpotekaBank(BaseBankClass):
    bank_name = 'Ipoteka bank'
    bank_slug = 'ipotekabank'

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
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class XalqBank(BaseBankClass):
    bank_name = 'Xalq banki'
    bank_slug = 'xalqbank'

    @staticmethod
    def get_item_by_code(items, code):
        for item in items:
            if item['title'] == code:
                return item
        return None

    @classmethod
    def get_data(self):
        try:
            params = {
                '_f': 'json',
            }
            requests.packages.urllib3.disable_warnings()
            response = requests.get(
                'https://xb.uz/api/v1/external/client/default', params=params, verify=False)
            data = response.json()
            ex_data = self.get_item_by_code(data, 'USD')

            olish = float(ex_data.get('BUYING_RATE').replace(' ', ''))
            sotish = float(ex_data.get('SELLING_RATE').replace(' ', ''))

            return {
                'success': True,
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class QQBank(BaseBankClass):
    bank_name = 'Qishloq qurilish banki'
    bank_slug = 'qishloqqbbank'

    @staticmethod
    def get_item_by_code(items, code):
        for item in items:
            if item['slug'] == code:
                return item
        return None

    @classmethod
    def get_data(self):
        try:
            requests.packages.urllib3.disable_warnings()
            response = requests.get(
                'https://manage.qishloqqurilishbank.uz/api/currency-rates/last', verify=False)
            data = response.json()['data']['currency_rate']['currencies']
            ex_data = self.get_item_by_code(data, 'USD')

            olish = ex_data.get('buy_rate')
            sotish = ex_data.get('sell_rate')

            return {
                'success': True,
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class NationalBank(BaseBankClass):
    bank_name = 'Milliy bank'
    bank_slug = 'nbubank'

    @staticmethod
    def get_item_by_code(items, code):
        for item in items:
            if item['code'] == code:
                return item
        return None

    @classmethod
    def get_data(self):
        try:
            response = requests.get('https://nbu.uz/uz/exchange-rates/json/')
            data = response.json()
            ex_data = self.get_item_by_code(data, 'USD')
            olish = float(ex_data['nbu_buy_price'])
            sotish = float(ex_data['nbu_cell_price'])

            return {
                'success': True,
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class SQBank(BaseBankClass):
    bank_name = 'Sanoat qurilish bank'
    bank_slug = 'sqbbank'

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

            data = data['data']['offline']
            ex_data = self.get_item_by_code(data, 'USD')

            olish = ex_data['buy']//100
            sotish = ex_data['sell']//100

            return {
                'success': True,
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


class sdfgfSQBank(BaseBankClass):
    bank_name = 'Sanoxcxcat qurilish bank'
    bank_slug = 'sqbbxcank'

    @staticmethod
    def get_item_by_code(items, code):
        for item in items:
            if item['code'] == code:
                return item
        return None

    @classmethod
    def get_data(self):
        try:
            cookies = {
                '_ga': 'GA1.1.523508631.1682585902',
                'smart_top': '1',
                'PHPSESSID': 'a59f8ef13bf330882e9e40af73166aa4',
                '_ga_RQHSFQHPM6': 'GS1.1.1685450316.5.1.1685450354.0.0.0',
                '__atuvc': '0%7C18%2C0%7C19%2C0%7C20%2C4%7C21%2C2%7C22',
                '__atuvs': '6475ee4d70da869c001',
            }

            headers = {
                'authority': 'xb.uz',
                'accept': 'application/json',
                'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
                # 'cookie': '_ga=GA1.1.523508631.1682585902; smart_top=1; PHPSESSID=a59f8ef13bf330882e9e40af73166aa4; _ga_RQHSFQHPM6=GS1.1.1685450316.5.1.1685450354.0.0.0; __atuvc=0%7C18%2C0%7C19%2C0%7C20%2C4%7C21%2C2%7C22; __atuvs=6475ee4d70da869c001',
                'referer': 'https://xb.uz/ru/page/physical/',
                'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57',
            }

            params = {
                '_f': 'json',
            }

            response = requests.get('https://xb.uz/api/v1/external/client/default',
                                    params=params, cookies=cookies, headers=headers)
            data = response.json()

            data = data['data']['offline']
            ex_data = self.get_item_by_code(data, 'USD')

            olish = ex_data['buy']//100
            sotish = ex_data['sell']//100

            return {
                'success': True,
                'bank_slug': self.bank_slug,
                'olish': olish,
                'sotish': sotish
            }
        except Exception as e:
            print(e.args)
            return {
                'success': False
            }


# deyarli jsonli data
