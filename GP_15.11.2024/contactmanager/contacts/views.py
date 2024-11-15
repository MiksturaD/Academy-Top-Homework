from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import title
from contact.models import Contact
from .forms import ContactForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts,
                                                 'name': name, 'email': email})


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')  # Redirect to the contact list page after adding
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')  # Redirect to the contact list page after deleting
    return render(request, 'delete_contact.html', {'contact': contact})