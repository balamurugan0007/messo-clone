from django.db import models


# Create your models here.


class info(models.Model):
    Name=models.CharField(max_length=100,blank=False,null=False)
    email=models.EmailField(max_length=100,blank=False,null=False)
    pass1=models.CharField(max_length=100,blank=False,null=False)


    def __str__(self) :
        return self.Name


class catogory(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    image=models.ImageField(upload_to='static/products',null=False,blank=False)
    description=models.TextField(max_length=300,null=False,blank=False)
    date=models.DateField()
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")

    def __str__(self) :
        return self.name
    



class products(models.Model):
    catogory=models.ForeignKey(catogory,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,blank=False,null=False)
    #brand=models.CharField(max_length=170)
    old_price=models.IntegerField(blank=False,null=False)
    new_price=models.IntegerField(blank=False,null=False)
    ratings=models.FloatField(blank=False,null=False)
    stocks=models.IntegerField(blank=False,null=False)
    
    image=models.ImageField(upload_to='static/products',null=False,blank=False)
    description=models.TextField(max_length=300,null=False,blank=False)
    date=models.DateField()
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    

    def __str__(self) :
        return self.name
    
class favourite(models.Model):
    user=models.ForeignKey(info,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

class addcart(models.Model):
    user=models.ForeignKey(info,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)   