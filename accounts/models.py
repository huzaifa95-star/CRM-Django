from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user= models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name= models.CharField(max_length=200, null=True)
    phone= models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200, null=True)
    profile_pic= models.ImageField(default='#',null=True, blank=True)
    date_ordered= models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name or ''

   

class Tag(models.Model):
    name= models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name or ''

class Product(models.Model):
    CATEGORY=(
        ('indoor',"indoor"),
        ('outdoor',"outdoor"),
        
    )
    name= models.CharField(max_length=200, null=True)
    price= models.FloatField(null=True)
    category=models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_ordered= models.DateTimeField(auto_now_add=True, null=True)
    tag=models.ManyToManyField(Tag)

    def __str__(self):
        return self.name or ''



class Order(models.Model):
    STATUS=(
        ('pending',"pending"),
        ('out of delivery',"out of delivery"),
        ('delivered',"delivered"),
    )
    customer=models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    date_ordered= models.DateTimeField(auto_now_add=True, null=True)
    status=models.CharField(max_length=200,choices=STATUS)
    
    def __str__(self):
        return self.product.name or ''