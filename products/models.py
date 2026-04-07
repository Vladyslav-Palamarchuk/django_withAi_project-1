from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    ai_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.title} - {self.price} грн."


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order')
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Замовлення {self.product.title} від {self.customer_name}"

