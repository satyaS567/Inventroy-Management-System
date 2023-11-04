from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=200,null=True)
    purchaseitems = models.IntegerField()
    solditems = models.IntegerField()
    itempiece = models.IntegerField()
    sales = models.IntegerField()
    purchasedate = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.productname