from django.db import models
from users.models import User
from products.models import Product


class CartItem(models.Model):
    cart = models.OneToOneField('Cart', on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cartItems= models.ManyToManyField(CartItem, related_name='wishlists')

    
    
