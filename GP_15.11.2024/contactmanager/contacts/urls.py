from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name="main"),
    path('', views.contact_list, name='contact list'),
    path('add/', views.add_contact, name='add contact'),
    path('delete/<int:id>/', views.delete_contact, name="delete contact"),
]