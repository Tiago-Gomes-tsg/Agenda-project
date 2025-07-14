from django.urls import path
from contacts.views import contact_views


app_name = 'contacts'

urlpatterns = [
    path('', contact_views.index, name='contact'),
    path('contact/', contact_views.index, name='contact'),
    path('contacts/', contact_views.index, name='contact'),
]