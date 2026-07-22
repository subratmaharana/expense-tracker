from django import forms
from .models import IncomeSource ,Budget

class IncomeSourceForm(forms.ModelForm):

    class Meta:
        model=IncomeSource
        fields=["source","amount","date"]
        widgets={
            "date":forms.DateInput(attrs={"type":"date"})
        }
    
class BudgetForm(forms.ModelForm):

    class Meta:
        model=Budget
        fields=["amount"]