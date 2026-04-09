from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order


@receiver(post_save, sender=Order)
def notify_admin_on_new_order(sender, instance, created, **kwargs):
    if created:
        print(f"Сигнал: Нове замовлення! Клієнт {instance.customer_name}"
              f" купив {instance.product.title}")

