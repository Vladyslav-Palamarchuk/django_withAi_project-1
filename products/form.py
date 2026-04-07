from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_phone', 'quantity']


        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше ім\'я'
            }),
            'customer_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+380...'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
        }
        labels = {
            'customer_name': "Ваше ім'я",
            'customer_phone': "Номер телефону",
            'quantity': "Кількість",
        }


    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity > 5:
            raise forms.ValidationError("Вибачте, кількість до 5 одиниць.")
        return quantity
