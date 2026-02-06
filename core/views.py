from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

# Base
# Index
# /about-us
# /contact
# /pricing
# /restaurants
# /restaurants/_____