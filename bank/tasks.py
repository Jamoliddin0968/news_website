from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime
from bank.banks.master import get_all_data


@shared_task(name="updated_bank_data")
def update_bank_data(*args, **kwargs):
    get_all_data()
    return {"ok": True}

from datetime import time
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'hello-world-daily': {
        'task': 'tasks.hello_world',
        'schedule': crontab(hour=9, minute=30),
    },
}