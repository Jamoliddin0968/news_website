
from .infinbank import (
    TuronBank, InfinBank, AgroBank, HamkorBank, IpakYuliBank, MikroKreditBank, SQBank,
    OFBank, TrustBank, ZiraatBank, KapitalBank, UniversalBank, AsakaBank, IpotekaBank, GarantBank, AABBank, AloqaBank
)

bank_list = (
    TuronBank, InfinBank, AgroBank, HamkorBank, IpakYuliBank, MikroKreditBank, SQBank,
    OFBank, TrustBank, ZiraatBank, KapitalBank, UniversalBank, AsakaBank, IpotekaBank, GarantBank, AABBank, AloqaBank
)


# def get_all_data(daily):
#     from bank.models import Exchange as ex

#     data = []

#     for i in bank_list:
#         temp_data = i().get_data()
#         if temp_data["success"]:
#             bank_name = temp_data['bank_name']
#             olish = int(temp_data['olish'])

#             sotish = int(temp_data['sotish'])
#             ex.objects.create(
#                 daily=daily,
#                 bank_name=bank_name,
#                 buy=olish, sell=sotish
#             )
#             data.append(temp_data)
#     return data

import threading


def get_data_and_save(bank, daily):
    from bank.models import Exchange as ex
    temp_data = bank().get_data()
    if temp_data["success"]:
        bank_name = temp_data['bank_name']
        olish = int(temp_data['olish'])
        sotish = int(temp_data['sotish'])
        ex.objects.create(
            daily=daily,
            bank_name=bank_name,
            buy=olish,
            sell=sotish
        )
        return temp_data
    return None

def get_all_data(daily):
    # bank_list = [Bank1, Bank2, Bank3]  # Bank1, Bank2, Bank3 gibi banka sınıflarını burada tanımlamanız gerekiyor

    threads = []
    results = []

    for bank in bank_list:
        thread = threading.Thread(target=lambda: results.append(get_data_and_save(bank, daily)))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return results
