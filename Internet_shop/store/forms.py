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
            'name': 'Название категории',
        }

    def __init__(self, *args, **kwargs):
        super(CategoryCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'aria-label': 'Название категории'})



class OrderCreateForm(forms.ModelForm):
  class Meta:
    model = Order
    fields = ['customer_name', 'customer_email', 'order_date', 'line']
    widgets = {
      'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
      'customer_email': forms.EmailInput(attrs={'class': 'form-control'}),
      'order_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
      'line': forms.SelectMultiple(attrs={'class':'form-select'})
    }
    labels = {
        'customer_name':'Имя клиента',
        'customer_email':'Е-майл клиента',
        'order_date':'Дата заказа',
        'line': 'Продукты',
    }

  def __init__(self, *args, **kwargs):
    super(OrderCreateForm, self).__init__(*args, **kwargs)
    self.fields['customer_name'].widget.attrs.update({'aria-label': 'Имя клиента'})
    self.fields['customer_email'].widget.attrs.update({'aria-label': 'Е-майл клиента'})
    self.fields['order_date'].widget.attrs.update({'aria-label': 'Дата заказа'})
    self.fields['line'].widget = forms.CheckboxSelectMultiple()
    self.fields['line'].queryset = Product.objects.all()


class ProductCreateForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ['name', 'description', 'price', 'is_available', 'category']
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'description': forms.TextInput(attrs={'class': 'form-control'}),
      'price': forms.NumberInput(attrs={'class': 'form-control'}),
      'category': forms.Select(attrs={'class':'form-select'})
    }
    labels = {
        'name':'Название товара',
        'description':'Описание',
        'price':'Цена',
        'category': 'Категория',
    }

  def __init__(self, *args, **kwargs):
    super(ProductCreateForm, self).__init__(*args, **kwargs)
    self.fields['name'].widget.attrs.update({'aria-label': 'Название товара'})
    self.fields['description'].widget.attrs.update({'aria-label': 'Описание'})
    self.fields['price'].widget.attrs.update({'aria-label': 'Цена'})
    self.fields['category'].queryset = Category.objects.all()