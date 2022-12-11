from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import get_defillama_data


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_defillama_data, 'interval', seconds=15)
    scheduler.start()
