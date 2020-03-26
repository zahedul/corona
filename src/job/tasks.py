from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery import shared_task
from celery.utils.log import get_task_logger
from datetime import timedelta

from time import sleep
 
logger = get_task_logger(__name__)

@periodic_task(run_every=timedelta(seconds=1))
def task_one():
    sleep(2)
    logger.info("Task started")
    # add code
    logger.info("Task finished")

@periodic_task(run_every=timedelta(seconds=1))
def task_two():
    sleep(3)
    logger.info("Task started")
    # add code
    logger.info("Task finished")