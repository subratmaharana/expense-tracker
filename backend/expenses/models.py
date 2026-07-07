from django.db import models

# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transaction(models.Model):

    TRANSACTION_TYPES = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    ]

    title = models.CharField(max_length=150)
 
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    description = models.TextField(blank=True)

    def __str__(self):
        return self.title        