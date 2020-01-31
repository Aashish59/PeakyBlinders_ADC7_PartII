from django.db import models

# Create your models here.
class Post(models.Model):     
                                                               
    content = models.CharField(max_length=256)                                                 
    created_at = models.DateTimeField('Datetime created')           

    def __str__(self):
        return self.content

class Comment(models.Model):                                                                   
    post = models.ForeignKey('Post', on_delete=models.CASCADE)                                                             
    message = models.TextField()                                                               
    created_at = models.DateTimeField('Datetime created')
                                                                                    
