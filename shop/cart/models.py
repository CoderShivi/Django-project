from django.db import models
# 1. Product id
from mainapp.models import Product
# 2. user id
from django.contrib.auth.models import User

# Create your models here.
class CartItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=0)
    date_added =models.DateField(auto_now_add=True)

    # string representation of cartItem object
    def __str__(self):
        return f"Product: {self.product.name} -Count: {self.quantity}"
    
    # Method to find total price of particular item in cart
    def get_total_price(self):
        return self.quantity * self.product.price