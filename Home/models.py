from django.db import models
from portfolio.models import Project

class TeamMember(models.Model):
    
    full_name = models.CharField(max_length=200, verbose_name="نام و نام خانوادگی")
    job  = models.CharField(max_length=100, verbose_name="سمت")
    image = models.ImageField(upload_to="images/team", verbose_name="تصویر ")
    
    instagram = models.URLField(blank=True, verbose_name="اینستاگرام")
    linkedin_url = models.URLField(blank=True, verbose_name="لینکدین")
    twitter_url = models.URLField(blank=True, verbose_name="توییتر")
    
    #class Meta:
        #verbose_name = "اعضای تیم"
    
    def __str__(self):
        return self.full_name

class ContactUs(models.Model):
    
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=11, blank=False, null=False)
    text = models.TextField(null=False, blank=False)
    
    def __str__(self):
        return f"{self.name} - {self.text[:30]}"
    
class CompanyStats(models.Model):
    years_experience = models.PositiveIntegerField(verbose_name="سال تجربه")
    happy_clients = models.PositiveIntegerField(verbose_name="مشتریان راضی")
    service_hours = models.PositiveIntegerField(verbose_name="ساعت خدمات")
    successful_projects = models.PositiveIntegerField(verbose_name="پروژه موفق", blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.successful_projects is None:
            self.successful_projects = Project.objects.filter(status="پایان یافته").count()
        super(CompanyStats, self).save()
        
    def __str__(self):
        return "company stats"
