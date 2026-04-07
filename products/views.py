from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Product
from django.contrib import messages
from .form import OrderForm



# Create your views here.

class ProductListView(ListView):
    model = Product
    templates_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    templates_name = 'product/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm()
        return context

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = self.get_object()
            order.save()
            messages.success(request, f"Дякуємо, {order.customer_name}! Замовлення прийнято.")
            return redirect('product-detail', pk=order.product.pk)


