from django.http import HttpResponse
from shop.tasks import works_with_date
from datetime import timedelta, datetime
from django_celery_beat.models import PeriodicTask


def hello(request):
    n = int(request.GET.get("n"))
    # works_with_date.delay(n)
    works_with_date(n)
    # works_with_date.apply_async(
    #     eta=datetime.now() + timedelta(seconds=20),
    #     kwargs={
    #         "n": n
    #     }
    # )
    # works_with_date.apply_async(
    #     countdown=10,
    #     kwargs={"n": n}
    # )
    # works_with_date.apply_async(
    #     countdown=10,
    #     expires=5,
    #     kwargs={"n": n}
    # )
    return HttpResponse("hello world")

# celery -A testcel worker 5 -l INFO -B
# W = CPU * 2 + 1
