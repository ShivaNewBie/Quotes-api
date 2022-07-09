from django.db import models

from django.contrib.auth.models import User 

# Create your models here.

class Quote(models.Model):
    quote_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quote_body = models.CharField(max_length=250)
    context = models.CharField(max_length=250)
    source = models.URLField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.quote_author)
