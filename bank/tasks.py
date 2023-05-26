from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime, timedelta
from bank.banks.master import get_all_data


@shared_task
def update_bank_data(*args, **kwargs):
    print("wertyu")
    # get_all_data()
    return {"ok": True}



