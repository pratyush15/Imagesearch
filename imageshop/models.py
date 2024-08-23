from tkinter import CASCADE
from django.db import models

#Create model category 
class Category(models.Model): 
    title=models.CharField(max_length=100) 
    desc=models.TextField()

#Create model image 
class Image(models.Model): 
    title=models.CharField(max_length=100)   
    desc=models.TextField()   
    image=models.ImageField(upload_to="images") 
    added_date=models.DateTimeField() 
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)  

    def __str__(self): 
        return self.title
