# Imports
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Internal:
# Status of a inspo item, draft or published
STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Inspo(models.Model):
    """
    This model is for a inspo item
    """
    class Meta:
        ordering = ['-create_date']

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=250,
        unique=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='inspo_items'
    )
    inspo_item_text = models.TextField(
        max_length=500,
    )
    image = models.ImageField(
        null=True,
        blank=True
    )
    update_date = models.DateTimeField(
        auto_now=True
    )
    create_date = models.DateTimeField(
        auto_now_add=True
    )
    status = models.IntegerField(
        choices=STATUS,
        default=0
    )

    def __str__(self):
        """
        Return new title string
        Args:
            self (object): self
        Returns:
            inspo title
        """
        return self.title
