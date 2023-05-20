
from .infinbank import (
    TuronBank, InfinBank, AgroBank, HamkorBank, IpakYuliBank, MikroKreditBank, SQBank,
    OFBank, TrustBank, ZiraatBank, KapitalBank, UniversalBank, AsakaBank, IpotekaBank, GarantBank, AABBank, AloqaBank
)

bank_list = (
    TuronBank, InfinBank, AgroBank, HamkorBank, IpakYuliBank, MikroKreditBank, SQBank,
    OFBank, TrustBank, ZiraatBank, KapitalBank, UniversalBank, AsakaBank, IpotekaBank, GarantBank, AABBank, AloqaBank
)


def get_all_data(daily):
    from bank.models import Exchange as ex

    data = []

    for i in bank_list:
        temp_data = i().get_data()
        if temp_data["success"]:
            bank_name = temp_data['bank_name']
            olish = int(temp_data['olish'])

            sotish = int(temp_data['sotish'])
            ex.objects.create(
                daily=daily,
                bank_name=bank_name,
                buy=olish, sell=sotish
            )
            data.append(temp_data)
    return data
