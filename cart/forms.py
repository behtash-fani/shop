from django import forms



class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'0'}))