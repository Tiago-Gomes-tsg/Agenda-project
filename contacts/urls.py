from django.urls import path
from contacts.views import *


app_name = 'contacts'

urlpatterns = [
    path('<int:contact_id>/', contact_views.contact, name='contact'),
    path('search/', contact_views.search, name='search'),
    path('', contact_views.index, name='index'),
]