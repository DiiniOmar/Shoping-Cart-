from django import forms 

class ItemAddForm(forms.Form):
    itemname= forms.CharField( max_length= 20)
    itemQuantity = forms.IntegerField()