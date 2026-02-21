from django.shortcuts import render
from django.core.mail import send_mail

from restaurant.models import Restaurant, MenuItems, MENU_ITEMS_CATEGORY_CHOICES

def index(request):
    all_restaurants = Restaurant.objects.all()
    ctx = {
        'all_restaurants': all_restaurants
    }
    return render(request, 'index.html', ctx)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "GET":
        return render(request, 'contact.html')
    else:
        name = request.POST.get('emri')
        email = request.POST.get('email')
        nr_tel = request.POST.get('nr_cel')
        mesazhi = request.POST.get('mesazhi')
        
        send_mail(
            "Pershendetje, ke nje kontakt te ri",
            f"""
            Pershendetje Martin, ke nje kontakt te ri tek
            faqja juaj. Kontakti eshte: {name} me email {email}.
            Numri i telefonit eshte {nr_tel}. Personi ka
            shkruar kete mesazh: {mesazhi}
            """,
            "lagjimartin@gmail.com",
            ["ajlameta08@gmail.com"],
            fail_silently=False,
        )

        send_mail(
            f"Pershendetje {name}, e morem mesazhin tuaj.",
            f"""
            Kerkesa juaj u mor dhe do te procesohet. Do ju kontaktoje stafi
            yne brenda 24-48 oresh. Diten e mire.
            """,
            "lagjimartin@gmail.com",
            [email],
            fail_silently=False
        )

        ctx = {
            'sukses': True
        }
        return render(request, 'contact.html', ctx)

def pricing(request):
    return render(request, 'pricing.html')

def restaurant_menu(request, pk):
    restaurant_items = MenuItems.objects.filter(
        restaurant = pk
    )
    
    categories = []
    for c in MENU_ITEMS_CATEGORY_CHOICES:
        categories.append(c[0])
    
    ctx = {
        'restaurant_items': restaurant_items,
        'categories': categories
    }

    return render(request, 'restaurant_menu.html', ctx)

def search_results(request):
    search_term = request.GET.get('search')
    searched_items = MenuItems.objects.filter(
        name__icontains=search_term
    )

    ctx = {
        'searched_items': searched_items
    }

    return render(request, 'search_results.html', ctx)