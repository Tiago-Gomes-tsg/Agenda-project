from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
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

def search(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            search_value = request.GET.get('q', '').strip()
            if search_value == '':
                return redirect('contacts:index')
            contacts = Contact.objects.filter(user=request.user)\
                .filter(Q(first_name__icontains=search_value), Q(last_name__icontains=search_value), Q())\
                .order_by('-id')[:20]
            context = {
                'contacts': contacts,
            }
        else:
            context= {
                'contacts': [],
            }
        return render(request, 'contacts/index.html', context)
    else:
        from django.http import HttpResponseNotAllowed
        return HttpResponseNotAllowed(['GET'])
    