from django.db import models

# Create your models here.

class Product(models.Model):
    asin = models.CharField(primary_key= True, max_length=50)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=2000)
    partition = models.IntegerField(blank= True)
    ccScore = models.DecimalField(blank= True, default=0, decimal_places = 5,max_digits = 7 )
    created_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.asin+": "+ self.title 