from django.db import models
from cart.models import Cart
from users.models import User
from enum import Enum

class PaymentStatus(Enum):
    Stripe = 'Stripe'
    CashOnDelivery = 'CashOnDelivery'
    
# Create your models here.
class Order(models.Model):
    cart=models.OneToOneField(Cart, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    address=models.CharField(max_length=200),
    postalNo=models.IntegerField()
    localAddress=models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=[(status.name, status.value) for status in PaymentStatus])
    is_active = models.BooleanField(default=True)
    is_delivered = models.BooleanField(default=False)
    