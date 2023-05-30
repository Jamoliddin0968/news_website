import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

from django.core.cache import cache

from bank.models import Bank, Daily

from .infinbank import (AABBank, AgroBank, AloqaBank, AsakaBank, GarantBank,
                        HamkorBank, InfinBank, IpakYuliBank, IpotekaBank,
                        KapitalBank, MadadInvestBank, MikroKreditBank,
                        NationalBank, OFBank, QQBank, SQBank, TrustBank,
                        TuronBank, UniversalBank, XalqBank, ZiraatBank)

bank_list = (
    TuronBank, InfinBank, AgroBank, HamkorBank, IpakYuliBank, MikroKreditBank, SQBank,
    OFBank, TrustBank, ZiraatBank, KapitalBank, UniversalBank, AsakaBank, IpotekaBank,
    GarantBank, AABBank, AloqaBank, XalqBank, QQBank, MadadInvestBank, NationalBank
)


def get_data(bank, daily):
    from bank.models import Exchange as ex
    temp_bank = bank()
    t1 = datetime.now()
    temp_data = temp_bank.get_data()
    if temp_data["success"]:
        bank_slug = temp_data['bank_slug']
        current_bank = Bank.objects.filter(slug=bank_slug).first()
        if not current_bank:
            current_bank = Bank.objects.create(
                slug=bank_slug,
                name=temp_bank.bank_name
            )
        olish = int(temp_data['olish'])
        sotish = int(temp_data['sotish'])
        new_obj = ex(
            daily=daily,
            bank=current_bank,
            buy=olish,
            sell=sotish
        )
        return new_obj
    else:
        print(temp_bank.bank_name)
    return None


def get_all_data():
    from bank.models import Exchange as ex
    t1 = datetime.now()
    daily = Daily.objects.create()
    data = []
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_data, bank, daily)
                   for bank in bank_list]

        for future in as_completed(futures):
            temp_data = future.result()
            if temp_data:
                data.append(temp_data)

    ex.objects.bulk_create(data)
    print(datetime.now()-t1)
    cache.delete('currency_data')
    return True
