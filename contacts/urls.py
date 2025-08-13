from django.urls import path
from contacts.views import *


app_name = 'contacts'

urlpatterns = [
    path('search/', contact_views.search, name='search'),
    path('', contact_views.index, name='index'),
    
    #CRUD
    path('contact/<int:contact_id>/detail/', contact_views.contact, name='contact'),
    path('contact/create/', contact_views.create, name='create'),
    path('contact/<int:contact_id>/update/', contact_views.update, name='update'),
]