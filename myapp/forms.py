from django.forms import ModelForm
from core.models import Expense


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'amount', 'category')
