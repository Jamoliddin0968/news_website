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


def bank_dict() -> dict:
    bank_dict_list = {}
    banks = Bank.objects.all()
    for bank in banks:
        bank_dict_list[bank.slug] = bank.id
    return bank_dict_list


def get_data(bank, daily_id, bank_id):
    from bank.models import Exchange as ex
    temp_bank = bank()
    temp_data = temp_bank.get_data()
    if temp_data["success"]:
        bank_slug = temp_data['bank_slug']
        if not bank_id:
            current_bank = Bank.objects.create(
                slug=bank_slug,
                name=temp_bank.bank_name
            )
            bank_id = current_bank.id
        olish = int(temp_data['olish'])
        sotish = int(temp_data['sotish'])
        new_obj = ex(
            daily_id=daily_id,
            bank_id=bank_id,
            buy=olish,
            sell=sotish
        )
        return new_obj
    else:
        print(temp_bank.bank_name)
    return None


def get_all_data():
    from bank.models import Exchange as ex
    daily = Daily.objects.create()
    bank_id_list = bank_dict()
    data = []
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_data, bank, daily.id, bank_id_list.get(bank().bank_slug))
                   for bank in bank_list]

        for future in as_completed(futures):
            temp_data = future.result()
            if temp_data:
                data.append(temp_data)

    ex.objects.bulk_create(data)
    daily.completed = True
    daily.save()
    cache.delete('currency_data')
    return True
