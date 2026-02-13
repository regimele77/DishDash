from django.shortcuts import render
from restaurant.models import Restaurant
from django.core.mail import send_mail

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
            "",
            [""],
            fail_silently=False,
        )

        send_mail(
            f"Pershendetje {name}, e morem mesazhin tuaj.",
            f"""
            Kerkesa juaj u mor dhe do te procesohet. Do ju kontaktoje stafi
            yne brenda 24-48 oresh. Diten e mire.
            """,
            "",
            [email],
            fail_silently=False
        )

        ctx = {
            'sukses': True
        }
        return render(request, 'contact.html', ctx)

def pricing(request):
    return render(request, 'pricing.html')
