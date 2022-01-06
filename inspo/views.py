# Imports
# 3rd party:
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

# Internal:
from .forms import InspoForm
from .models import Inspo


def inspo_items(request):
    """
    A view to show all inspo items
    The context contains the inspo_items_published
    and inspo_items_drafts
    Args:
        request (object): HTTP request object.
    Returns:
        Renders the inspo page.
    """
    inspo_items_published = \
        Inspo.objects.filter(status=1).order_by('-create_date')
    inspo_items_drafts = \
        Inspo.objects.filter(status=0).order_by('-create_date')

    inspo_items_count = Inspo.objects.filter(status=1).count()

    context = {
        'inspo_items_published': inspo_items_published,
        'inspo_items_drafts': inspo_items_drafts,
        'inspo_items_count': inspo_items_count
    }

    return render(request, 'inspo/inspo.html', context)


def manage_inspo_items(request):
    """
    A view to manage all inspo items
    Args:
        request (object): HTTP request object.
    Returns:
        Renders the manage inspo item page.
    """
    all_inspo_items = Inspo.objects.order_by('-create_date')
    inspo_items_count = Inspo.objects.filter().count()

    context = {
        'inspo_items': all_inspo_items,
        'inspo_items_count': inspo_items_count
    }

    return render(request, 'inspo/manage_inspo_items.html', context)


@login_required
def add_inspo_item(request):
    """
    A view to add a inspo_item
    Args:
        request (object): HTTP request object.
    Returns:
        Renders the add inspo item page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        inspo_form = InspoForm(request.POST, request.FILES)
        if inspo_form.is_valid():
            form_data = inspo_form.save(commit=False)
            form_data.user = request.user
            form_data.save()
            messages.success(
                request, 'Your inspo item was posted successfully!')
            return redirect('inspo_items')
        else:
            messages.error(
                request, 'Your inspo item failed to add, Please try again')
            return redirect('add_inspo_item')
    else:
        inspo_form = InspoForm()

    template = 'inspo/add_inspo_item.html'
    context = {
        'post_form': inspo_form,
    }
    return render(request, template, context)


@login_required
def edit_inspo_item(request, inspo_item_id):
    """
    A view to editing inspo items
    Args:
        request (object): HTTP request object.
        inspo_item_id: inspo item id
    Returns:
        Renders the edit inspo item page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    inspo_item_to_edit = get_object_or_404(Inspo, pk=inspo_item_id)
    if request.method == 'POST':
        inspo_form = InspoForm(
            request.POST, request.FILES, instance=inspo_item_to_edit)
        if inspo_form.is_valid():
            inspo_form.save()
            messages.success(
                request, f'{inspo_item_to_edit.title} '
                f'was successfully updated')
            return redirect('manage_inspo_items')
        else:
            messages.error(
                request, f'Error, {inspo_item_to_edit.title} \
                was not successfully updated')
    else:
        inspo_form = InspoForm(instance=inspo_item_to_edit)
        messages.info(
            request, f'You are currently editing '
            f'{inspo_item_to_edit.title}')
    template = 'inspo/edit_inspo_item.html'
    context = {
        'inspo_form': inspo_form,
        'inspo_item': inspo_item_to_edit,
    }

    return render(request, template, context)


@login_required
def delete_inspo_item(request, inspo_item_id):
    """ Delete a inspo from the store """
    inspo = get_object_or_404(Inspo, pk=inspo_item_id)
    inspo.delete()
    messages.success(request, 'inspo deleted!')
    return redirect(reverse('manage_inspo_items'))


def inspo_item(request, inspo_item_id):
    """
    A view to show an individual inspo item
    Args:
        request (object): HTTP request object.
        inspo_item_id: inspo item id
    Returns:
        Renders the inspo item page
    """
    inspo_item = get_object_or_404(Inspo, pk=inspo_item_id)

    """ Adds comment to new item"""

    context = {
        'inspo_item': inspo_item,
    }

    return render(request, 'inspo/inspo_item.html', context)
