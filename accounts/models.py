

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE  )
 
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone= models.CharField(max_length=200, null=True,blank=True)
    profile_pic=models.ImageField(null=True,default='th.jpg' ,blank=True)
    date_created=models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self) -> str:
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self) -> str:
        return self.name
  
class Product (models.Model):
    category_choices= (
           ('indoor','indoor'),
           ('outdoor','outdoor'),
    )
    name= models.CharField(max_length=200, null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200, null=True, choices=category_choices)
    description=models.CharField(max_length=200, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    tag= models.ManyToManyField(Tag)


    def __str__(self) -> str:
        return self.name  
class Order(models.Model):
    status_choices =(
           ("pending","pending"),
           ("out for delivery","out for delivery"),
           ("delivered","delivered"),
          )
   
    customer=models.ForeignKey(Customer,null=True,on_delete= models.SET_NULL)
    product=models.ForeignKey(Product,null=True, on_delete= models.SET_NULL )
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    status=models.CharField(max_length=200, null=True, choices=status_choices)
    Note=models.CharField(max_length=1000, null=True)

    def __str__(self) -> str:
        return self.product.name  