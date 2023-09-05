import datetime
import time
from celery import shared_task
from django.db.models import F
from celery_singleton import Singleton
from django.db import transaction


@shared_task(base=Singleton)
def set_price(subscription_id):
    from services.models import Subscription  # cross import!!!

    with transaction.atomic():
        subscription = (
            Subscription.objects.select_for_update()
            .filter(id=subscription_id)
            .annotate(
                annotated_price=F("service__full_price")
                - F("service__full_price") * (F("plan__discount_percent") / 100.00)
            )
            .first()
        )  # price используем в агрегаторе
        subscription.price = subscription.annotated_price
        subscription.save()


@shared_task(base=Singleton)
def set_comment(subscription_id):
    from services.models import Subscription  # cross import!!!

    with transaction.atomic():
        subscription = Subscription.objects.select_for_update().get(id=subscription_id)
        subscription.comment = str(datetime.datetime.now())
        subscription.save()