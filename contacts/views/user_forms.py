from django.shortcuts import render, redirect
from contacts.forms import *

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:index')
    return render(request, 'contacts/register.html', {'form': form,})


def register_update(request):
    form = RegisterUpdateForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = RegisterUpdateForm(instance=request.user)
            if form.is_valid():
                form.save()
            
            return render(request, 'contacts/register.html', {'form': form,})
        
    return render(request, 'contacts/register.html', {'form': form,})