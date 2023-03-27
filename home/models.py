from django.db import models

class Blog(models.Model):
    Title = models.CharField(max_length=250)
    Text = models.TextField()
    Images=models.ImageField(upload_to='data/')
    Date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Title
   
    
class User(models.Model):
    email = models.EmailField(max_length=254)
    pwd = models.CharField(max_length=250)
    def __str__(self):
        return self.email
    
