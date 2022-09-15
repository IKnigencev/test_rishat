from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import JsonResponse
import stripe

from .models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY

YOUR_DOMAIN = 'http://127.0.0.1:8000'


def index(request):
    items = Item.objects.all()

    context = {
        'items': items
    }
    return render(request, 'main/index.html', context)


def buy_view(request, id):
    """Страница покупки."""
    item = get_object_or_404(Item, id=id)
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount_decimal': item.price,
                    'product_data': {
                        'name': item.name
                    }
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=YOUR_DOMAIN + '/success/',
        cancel_url=YOUR_DOMAIN + '/cancel/',
    )
    return JsonResponse({
        'id': checkout_session.id
    })


def item_profile(request, id):
    """Страница просмотра элемента."""
    model = get_object_or_404(Item, id=id)

    context = {
        'model': model,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'main/item_profile.html', context)
