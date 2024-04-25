from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=300)
    
    
    
class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imageUrl=models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    
    
    
    
    
    
    
    
    # one person    one  passport   --> models.OneToOneField(Person, on_delete=models.CASCADE)
    
    
    # author one    book many   --> models.ForeignKey(Author, on_delete=models.CASCADE, related_name='products')
    
    
    
    # manufacturer one   car many    -->models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    
    # student many course many ==> models.ManyToManyField(Student, related_name='courses')