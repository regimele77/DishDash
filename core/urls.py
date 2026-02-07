from django.urls import path
from .views import index, about, contact, pricing

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('pricing/', pricing, name='pricing')
]