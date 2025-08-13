from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from contacts.models import Contact
from django.urls import reverse
from django.db.models import Q
from contacts.forms import *

def index(request):
    if request.user.is_authenticated:
        contacts = Contact.objects.filter(user=request.user).order_by('-id')
        paginator = Paginator(contacts,25)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
        }
    else:
        context= {
            'page_obj': [],
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
                .filter(Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value) | Q(email__icontains=search_value)| Q(number__icontains=search_value))\
                .order_by('-id')
            paginator = Paginator(contacts,25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context = {
                'page_obj': page_obj,
            }
        else:
            context= {
                'page_obj': [],
            }
        return render(request, 'contacts/index.html', context)
    else:
        from django.http import HttpResponseNotAllowed
        return HttpResponseNotAllowed(['GET'])
    
def create(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ContactForm(request.POST)
            form_action = reverse('contacts:create')
            context = {
                'form': form,
                'form_action': form_action,
                'button_name': 'Criar',
            }
            if form.is_valid():
                contact = form.save(commit=False)
                contact.user=request.user
                contact.save()
                return redirect('contacts:contact', contact_id=contact.pk)
            
            return render(request, 'contacts/create.html', context)
    
    context = {
            'form': ContactForm(),
            'form_action': reverse('contacts:create'),
            'button_name': 'Criar',
        }
    return render(request, 'contacts/create.html', context)
    
def update(request, contact_id):
    contact = get_object_or_404(Contact,pk=contact_id, user=request.user)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ContactForm(request.POST, instance=contact)
            form_action = reverse('contacts:update', args=[contact.pk,])
            context = {
                'form': form,
                'form_action': form_action,
                'button_name': 'Atualizar',
            }
            if form.is_valid():
                contact = form.save(commit=False)
                contact.user=request.user
                contact.save()
                return redirect('contacts:contact', contact_id= contact.pk)
            
            return render(request, 'contacts/create.html', context)
    
    context = {
            'form': ContactForm(instance=contact),
            'form_action': reverse('contacts:update', args=[contact.pk]),
            'button_name': 'Atualizar',
        }
    return render(request, 'contacts/create.html', context)
