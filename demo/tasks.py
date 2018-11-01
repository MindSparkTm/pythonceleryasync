from __future__ import absolute_import
from celery import shared_task
from demo.models import Logs


@shared_task
def generate_logs(request, response):
    log = Logs(request=request,response=response)
    log.save()
