from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category')
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product')
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Sizecategory(models.Model):
    size=models.CharField(max_length=100)
    def __str__(self):
        return self.size

class ProductVariant(models.Model):
   csize = models.ForeignKey(Sizecategory,on_delete=models.CASCADE,null=True,blank=True)
    
