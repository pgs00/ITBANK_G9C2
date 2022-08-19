from django import forms
from .models import Prestamo


class PrestamosForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['loan_type', 'loan_date', 'loan_total', 'idCustomer']
