from django.db import models
    

class Category (models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Discount (models.Model):
    name=models.CharField(max_length=20)
    discount_percent=models.IntegerField()
    status=models.IntegerField()
    def __str__(self):
        return self.name

class AppManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(price=1000)

    # def get_queryset(self):
    #     return super().get_queryset().filter(Category="dashai")
    
    

class Product (models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    stock=models.IntegerField()
    description=models.CharField(max_length=100)
    image=models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    #object=models.Manager()
    app_object=AppManager()

    def __str__(self):
        return self.name






    
   

