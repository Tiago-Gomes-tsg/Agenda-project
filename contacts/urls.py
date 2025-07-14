from django.urls import path
from contacts.views import *


app_name = 'contacts'

urlpatterns = [
    path('contacts/', contact_views.index, name='contact'),
]