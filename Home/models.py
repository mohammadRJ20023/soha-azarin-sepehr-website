from django.db import models




class ContactUs(models.Model):
    
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=11, blank=False, null=False)
    text = models.TextField(null=False, blank=False)
    
    def __str__(self):
        return f"{self.name} - {self.text[:30]}"
