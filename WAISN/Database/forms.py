from django import forms
from .models import Product


# The form that allows the user to create a product and add it to the inventory
class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', "product_quantity"]
        widgets = {
            'product_quantity': forms.NumberInput(attrs={'class': 'num'}),
            'product_name': forms.TextInput(attrs={'placeholder': 'Apple'})

        }



# The form that allows the user to update the quantity of a product already
#   in the inventory
class UpdateProductForm(forms.ModelForm):

    class Meta:

        model = Product
        fields = ['product_name', 'product_quantity']
        widgets = {
            'product_name': forms.TextInput(attrs={'placeholder': 'Banana'}),
            'product_quantity': forms.NumberInput(attrs={'class': 'num'})
        }



# The form that allows the user to delete a product that is already in the
#   inventory
class DeleteProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name']
        widgets = {
            'product_name': forms.TextInput(attrs={'placeholder': 'Clementine'})
        }
