from django.shortcuts import render, get_object_or_404
from contacts.models import Contact


def index(request):
    if request.user.is_authenticated:
        contacts = Contact.objects.filter(user=request.user).order_by('-id')[:20]
        context = {
            'contacts': contacts,
        }
    else:
        context= {
            'contacts': [],
        }
    
    return render(request, 'contacts/index.html', context)

def contact(request, contact_id):
    if request.user.is_authenticated:
        single_contact = get_object_or_404(Contact, pk=contact_id)
        context = {
            'contact': single_contact,
        }
    else:
        context = {
            'contact': [],
        }
    
    return render(request, 'contacts/contact.html', context)