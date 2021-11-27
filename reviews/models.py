from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Review(models.Model):
    """
    A review model that allows users to perform
    CRUD operations on product reviews
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title