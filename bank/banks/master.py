
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
    data = [i().get_data() for i in bank_list if i().get_data()["success"]]

    exchanges = [ex(
        daily=daily,
        bank_name=temp_data['bank_name'],
        buy=int(temp_data['olish']),
        sell=int(temp_data['sotish'])
    ) for temp_data in data]

    ex.objects.bulk_create(exchanges)

    return data