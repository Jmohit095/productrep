from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50,default="", blank=True)
    descrip = models.CharField(max_length=250,default="Null")

    def __str__(self):
        return self.name
        


class Subcategory(models.Model):
    category = models.ForeignKey(Category,related_name='Sub_Category',on_delete=models.CASCADE,null=True,default="",blank=True) # type: ignore
    name = models.CharField(max_length=50,default="", blank=True)
    descrip = models.CharField(max_length=250,default="Null")
    def __str__(self):
        return self.name
        

class Product(models.Model):
    Category = models.ForeignKey(Category,related_name='Category',on_delete=models.CASCADE,null=True,default="",blank=True)
    Subcategory = models.ForeignKey(Subcategory,related_name='SubCategory',on_delete=models.CASCADE,null=True,default="",blank=True)
    name = models.CharField(max_length=50,default="", blank=True)
    img = models.ImageField(upload_to='productimage/',null=True,blank=True)
    size = models.IntegerField(default=0, blank=True) 
    qty = models.IntegerField(default=0, blank=True)
    colour = models.CharField(max_length=50,default="", blank=True)
    brand = models.CharField(max_length=250,default="Null")
    actual_amt = models.IntegerField(default=0, blank=True) 
    disc_amt = models.IntegerField(default=0, blank=True) 
    descrip = models.CharField(max_length=50,default="Null")
    def __str__(self):
        return self.name