from django.urls import path
from .views import index, about, contact, pricing, restaurant_menu, search_results

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('pricing/', pricing, name='pricing'),
    path('restaurant/<int:pk>/', restaurant_menu, name='restaurant_menu'),
    path('search_results/', search_results, name='search_results')
]