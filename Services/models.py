from django.db import models
from django.utils.text import slugify




class ExecutiveUnit(models.Model):
    
    name = models.CharField(max_length=100, verbose_name="نام واحد اجرایی")
    
    def __str__(self):
        
        return self.name
    
    

    
    
class Service(models.Model):
    title = models.CharField( null=False ,blank=False, verbose_name="عنوان")
    executive_unit =  models.ForeignKey(
        ExecutiveUnit,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="services",
        verbose_name="واحد اجرایی"
        )
    image = models.ImageField(upload_to="images/services")
    description = models.TextField(null=False, blank=False)
    task = models.CharField(verbose_name="خدمات اریه شده در پروژه")
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super().save()
    

    