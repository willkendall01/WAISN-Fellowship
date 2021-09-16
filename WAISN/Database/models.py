from django.db import models

# The model of a single Product which consists of two fields:
#       *product name (string, the primary key)
#       product quantity (int, with a default of 0)
class Product(models.Model):
    product_name = models.CharField(primary_key=True, max_length=200)
    product_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name + " (" + str(self.product_quantity) + ")"
