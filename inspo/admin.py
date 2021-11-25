# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal:
from .models import Inspo
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class InspoAdmin(admin.ModelAdmin):
    """
    Admin class for the Inspo model.
    """
    class Meta:
        verbose_name = 'Inspo'
        verbose_name_plural = 'Inspo'

    list_display = (
        'title',
        'user',
        'inspo_item_text',
        'image',
        'update_date',
        'create_date',
        'status',
    )
    list_filter = (
        'title',
        'user',
        'create_date',
    )
    search_fields = (
        'title',
        'user',
        'inspo_item_text',
        'image',
        'update_date',
        'create_date',
        'status',
    )

admin.site.register(Inspo, InspoAdmin)