import django_tables2 as tables
from .models import Product

# Uses the django_tables2 library to help format the site's table
#   Here, a the product table class is declared (used in views.py)
#   and it is given the class "mytable"


class ProductTable(tables.Table):
    class Meta:
        model = Product
        attrs = {"class": "mytable"}
