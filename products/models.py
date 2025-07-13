from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=128,unique=True)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return f"{self.name} ({self.id})"


class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to="product_images")
    description = models.TextField(null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=ProductCategory,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} ({self.id}) | категория: {self.category}"
