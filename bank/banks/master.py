import threading
from bank.models import Bank,Daily


from .infinbank import (AABBank, AgroBank, AloqaBank, AsakaBank, GarantBank,
                        HamkorBank, InfinBank, IpakYuliBank, IpotekaBank,
                        KapitalBank, MikroKreditBank, OFBank, SQBank,
                        TrustBank, TuronBank, UniversalBank,
                        ZiraatBank,XalqBank,QQBank,MadadInvestBank)

bank_list = (
    TuronBank, InfinBank, AgroBank, HamkorBank, IpakYuliBank, MikroKreditBank, SQBank,
    OFBank, TrustBank, ZiraatBank, KapitalBank, UniversalBank, AsakaBank, IpotekaBank,
    GarantBank, AABBank, AloqaBank,XalqBank,QQBank,MadadInvestBank
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



def get_data_and_save(bank, daily):
    from bank.models import Exchange as ex
    temp_bank = bank()
    temp_data = temp_bank.get_data()
    if temp_data["success"]:
        bank_slug = temp_data['bank_slug']
        current_bank=Bank.objects.filter(slug=bank_slug).first()
        if not current_bank:
            current_bank = Bank.objects.create(
                slug = bank_slug,
                name = temp_bank.bank_name
            )
        olish = int(temp_data['olish'])
        sotish = int(temp_data['sotish'])
        ex.objects.create(
            daily=daily,
            bank=current_bank,
            buy=olish,
            sell=sotish
        )
        return temp_data
    return None


def get_all_data():

    threads = []
    results = []
    daily = Daily.objects.create()
    for bank in bank_list:
        thread = threading.Thread(
            target=lambda: results.append(get_data_and_save(bank, daily)))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return True
