from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transaction(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    TRANSACTION_TYPES = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    ]

    title = models.CharField(max_length=150)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    paid_from = models.ForeignKey(
    "IncomeSource",
    on_delete=models.CASCADE,
    null=True,
    blank=True
    )

    date = models.DateField() 
    

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.title


class IncomeSource(models.Model):

    SOURCE_CHOICES = [
        ("Salary", "Salary"),
        ("Business", "Business"),
        ("Freelancing", "Freelancing"),
        ("Pocket Money", "Pocket Money"),
        ("Scholarship", "Scholarship"),
        ("Investment", "Investment"),
        ("Rental Income", "Rental Income"),
        ("Other", "Other"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    source = models.CharField(
        max_length=30,
        choices=SOURCE_CHOICES
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.source} - ₹{self.amount}"
    
class Budget(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    month=models.IntegerField()
    year=models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.month}/{self.year}"

