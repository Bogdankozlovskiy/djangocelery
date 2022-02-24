from time import sleep
from shop.models import Data
from celery import shared_task


@shared_task
def works_with_date(n):
    sleep(n)
    print("hello")
    Data.objects.create(title=f"hello {n}")
    return f"done {n}"
