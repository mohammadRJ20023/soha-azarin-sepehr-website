from django.db import models



class ExecutiveUnit(models.Model):
    
    name = models.CharField(max_length=100, verbose_name="نام واحد اجرایی")
    
    def __str__(self):
        
        return self.name
    
    

    
    
class Service(models.Model):
    title = models.CharField(null=False ,blank=False, verbose_name="عنوان")
    executive_unit =  models.ForeignKey(
        ExecutiveUnit,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="services",
        verbose_name="واحد اجرایی"
        )
    description = models.TextField(null=False, blank=False)
    
    def __str__(self):
        return self.title
    
class ServiceTask(models.Model):
    
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="tasks", 
        verbose_name="خدمات اریه شده در پروژه"
        )
    title = models.CharField(max_length=500, null=False, blank=False, verbose_name="عنوان")
    