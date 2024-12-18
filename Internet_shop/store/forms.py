from django import forms
from .models import Category, Product, Order


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'floatingCategory',
                'required': True
            }),
        }
        labels = {
            'name': 'Название категории',  # Добавляем метку для поля name
        }

    def __init__(self, *args, **kwargs):
        super(CategoryCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'aria-label': 'Название категории'})



class OrderCreateForm(forms.ModelForm):
  class Meta:
    model = Order
    fields = ['customer_name', 'customer_email', 'order_date']
    widgets = {
      'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
      'customer_email': forms.EmailInput(attrs={'class': 'form-control'}),
      'order_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    }