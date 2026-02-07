from django.db import models

RESTAURANT_CATEGORY_CHOICES = [
    ('Italian', 'Italian'),
    ('Sushi', 'Sushi'),
    ('Ushqime deti', 'Ushqime deti'),
    ('Tradicional', 'Tradicional'),
    ('Fast food', 'Fast food'),
    ('Pasticeri', 'Pasticeri'),
    ('Pica', 'Pica'),
]

RESTAURANT_PLAN = [
    ('Free', 'Free'),
    ('Platinium', 'Platinium'),
    ('Gold', 'Gold')
]

class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    address = models.CharField(max_length=150)
    opening_hours = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    delivery = models.BooleanField()
    rating = models.PositiveIntegerField()
    category = models.CharField(
        choices=RESTAURANT_CATEGORY_CHOICES
    )
    plan = models.CharField(
        choices=RESTAURANT_PLAN,
        default='Free'
    )
    email = models.EmailField()
    logo_link = models.URLField(default=None, blank=True)
    map_link = models.URLField(default=None, blank=True)
    facebook_link = models.URLField(default=None, blank=True)
    instagram_link = models.URLField(default=None, blank=True)
    tiktok_link = models.URLField(default=None, blank=True)
    web_link = models.URLField(default=None, blank=True)

    def __str__(self):
        return self.name