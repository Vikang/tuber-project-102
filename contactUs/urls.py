from django.urls import path
from contactUs import views

urlpatterns = [
    path('', views.contact, name='contact_us'),
    path('received', views.contact_received, name='sending_contact'),
]
