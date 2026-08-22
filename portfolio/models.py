from django.db import models
from django_jalali.db import models as jmodels 
import jdatetime
from django.utils.text import slugify



class Project(models.Model):
    
    STATUS_CHOICES = [
        ("پایان یافته", "پایان یافته"),
        ( "در حال اجرا", "در حال اجرا"),
        ("در انتظار اجرا", "در انتظار اجرا"),
    ]
    
    title = models.CharField(max_length=600, null=False, blank=False, verbose_name="عنوان پروژه")
    
    image = models.ImageField(upload_to='images/Projects', verbose_name="تصویر")
    
    project_type = models.CharField(max_length=100, null=False, blank=False, verbose_name="نوع پروژه")
    
    start_time = jmodels.jDateField(verbose_name="تاریخ شروع پروژه")
    
    end_time = jmodels.jDateField(verbose_name="تاریخ پایان پروژه", blank=True, null=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="وضعیت")
    
    about = models.TextField(verbose_name="درباره پروژه")
    
    created_at = jmodels.jDateField(auto_now_add=True)
    
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if  not self.slug :
            self.slug = slugify(self.title, allow_unicode=True)
        super(Project, self).save()
        
    @property
    def duration(self):
        
        end = self.end_time or jdatetime.date.today()
        return (end - self.start_time).days
    
    duration.fget.short_description = "مدت اجرا"

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