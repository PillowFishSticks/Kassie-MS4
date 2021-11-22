from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jyd4NBjBrwdhPcQC97swwqT9nYN5OxVK5oBrRa4abyLumPwHgFwri7IqFH727w3akthXysgS99sdZrNnDGo52lf00NxR9V2dP',
        'client_secret': 'intent.client_secret',
    }

    return render(request, template, context)
