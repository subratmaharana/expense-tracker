from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .models import Category


@receiver(post_migrate)
def create_default_categories(sender, **kwargs):

    if sender.name != "expenses":
        return

    default_categories = [
        "Food",
        "Travel",
        "Shopping",
        "Bills",
        "Entertainment",
        "Healthcare",
        "Education",
        "Rent",
        "Transport",
        "Other",
    ]

    for category in default_categories:
        Category.objects.get_or_create(
            name=category
        )