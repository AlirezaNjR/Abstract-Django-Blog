from django.db import models

class EmailSubscriptionsModel(models.Model):
    email = models.EmailField(max_length=254,null=False,blank=False,unique=True)
    
    class Meta:
        ordering = ['email']
        verbose_name = 'Email Subscription'
        verbose_name_plural = 'Email Subscriptions'
        
    def __str__(self) -> str:
        return f'{self.email}'
    