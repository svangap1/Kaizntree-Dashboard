# In your_app/models.py

from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Tag(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class Item(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    # tag = models.CharField(max_length = 20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock_status = models.BooleanField(default=True)
    available_stock = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "items"

    def __str__(self):
        return self.name if self.name else "Unnamed Item"
