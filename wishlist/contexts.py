# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.http import Http404
from django.shortcuts import get_object_or_404

# Internal:
from .models import Wishlist
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def wishlist_contents(request):
    """
    A context for wishlist to display count in users navbar
    Args:
        request (object): HTTP request object.
    Returns:
        context: context
    """
    try:
        wishlist = get_object_or_404(Wishlist, username=request.user.id)
        wishlist_items = wishlist.products.all()
        wishlist_count = len(wishlist_items)
    except Http404:
        wishlist_count = None

    context = {
        'wishlist_count': wishlist_count,
    }

    return context