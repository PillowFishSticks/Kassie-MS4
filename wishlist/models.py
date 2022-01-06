# Imports
# 3rd party:
from django.db import models
from django.contrib.auth.models import User

# Internal:
from products.models import Product


class Wishlist(models.Model):
    """
    This model is for a users Wishlist list
    """
    class Meta:
        verbose_name_plural = 'Wishlist'

    products = models.ManyToManyField(
        Product,
        blank=True
    )
    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """
        Return object string
        Args:
            self (object): self object.
        Returns:
            str: users favourite string
        """
        return f"{self.username}'s Wishlist"
