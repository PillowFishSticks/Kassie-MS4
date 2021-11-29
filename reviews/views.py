from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Review
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile


@login_required
def add_review(request, product_id):
    """ Add a review to an product """

    product = get_object_or_404(Product, pk=product_id)
    user = UserProfile.objects.get(user=request.user)

    review_form = ReviewForm(request.POST, request.FILES)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.user = user
        review.product = product
        review.title = request.POST["title"]
        review.description = request.POST["description"]
        review.save()

        product.save()

        messages.success(request, 'Successfully added review!')

        return redirect(reverse('product_detail', args=[product.id]))

    else:
        messages.error(
            request,
            'Failed to add review. Please ensure the form is valid.')

    return redirect(reverse('product_detail', args=(product_id,)))


@login_required
def edit_review(request, review_id):
    """ Allows users to edit their review """

    review = get_object_or_404(Review, pk=review_id)
    review_form = ReviewForm(request.POST, request.FILES, instance=review)
    product = get_object_or_404(Product, pk=review.product.pk)

    if review_form.is_valid():
        review.save()

        product.save()

        messages.success(request, 'Your review has been successfully edited')
    else:
        messages.error(
            request,
            'Failed to edit review. Please ensure the form is valid.')

    return redirect(reverse('product_detail', args=(review.product.id,)))


@login_required
def delete_review(request, review_id):
    """ Allows users to delete their review """

    review = get_object_or_404(Review, pk=review_id)
    product = get_object_or_404(Product, pk=review.product.pk)

    try:
        review.delete()

        product.save()

        messages.success(request, 'Your review has been successfully deleted')

    except Exception as e:
        messages.error(request,
                       "An error occured whilst trying to delete your review: "
                       f" error:{e}. Please try again later.")

    return redirect(reverse('product_detail', args=(review.product.id,)))