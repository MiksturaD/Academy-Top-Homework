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
        'aria-label': 'Название категории',
        'required': True
      }),
    }


class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['project', 'title', 'description', 'due_date', 'status']  # Все поля, которые можно редактировать
    widgets = {
      'project': forms.Select(attrs={'class': 'form-select'}),
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'description': forms.Textarea(attrs={'class': 'form-control'}),
      'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
      'status': forms.Select(attrs={'class': 'form-select'}),
    }