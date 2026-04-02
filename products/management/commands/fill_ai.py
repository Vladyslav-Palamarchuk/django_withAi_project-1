from django.core.management.base import BaseCommand
from products.models import Product
from products.services import generate_product_description
from django.db.models import Q

class Command(BaseCommand):
    help = "Автоматично заповнює опис товарів за допомогою ШІ"

    def handle(selfs, *args, **option):
        products = Product.objects.filter(ai_description__isnull=True)
        products = Product.objects.filter(
            Q(ai_description__isnull=True) | Q(ai_description="")
        )
        selfs.stdout.write(f"Знайдено {products.count()} товарів для обробки.")


        for product in products:
            selfs.stdout.write(f"Працюю над товаром: {product.title}...")
            try:
                new_description = generate_product_description(product.title)
                product.ai_description = new_description
                product.save()
                selfs.stdout.write(selfs.style.SUCCESS(f"Опис для '{product.title}' готовий!"))
            except Exception as e:
                selfs.stdout.write(selfs.style.ERROR(f"Помилка для {product.title}: {e}"))

        selfs.stdout.write(selfs.style.SUCCESS("Процес завершено успішно!"))








