from django.shortcuts import render
from restaurant.models import Restaurant

def index(request):
    all_restaurants = Restaurant.objects.all()
    ctx = {
        'all_restaurants': all_restaurants
    }
    return render(request, 'index.html', ctx)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def pricing(request):
    return render(request, 'pricing.html')

# Base
# Index
# /about-us
# /contact
# /pricing
# /restaurants
# /restaurants/_____