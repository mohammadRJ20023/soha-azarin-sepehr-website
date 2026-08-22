from django.db import models
from django_jalali.db import models as jmodels 
import jdatetime
from django.utils.text import slugify



class Project(models.Model):
    
    STATUS_CHOICES = [
        ("completed", "پایان یافته"),
        ("in_progress", "در حال اجرا"),
        ("pending", "در انتظار اجرا"),
    ]
    
    title = models.CharField(max_length=600, null=False, blank=False, verbose_name="عنوان پروژه")
    
    image = models.ImageField(upload_to='images/Projects', verbose_name="تصویر")
    
    type = models.CharField(max_length=100, null=False, blank=False, verbose_name="نوع پروژه")
    
    start_time = jmodels.jDateField(verbose_name="تاریخ شروع پروژه")
    
    end_time = jmodels.jDateField(verbose_name="تاریخ پایان پروژه", blank=True, null=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="وضعیت")
    
    created_at = jmodels.jDateField(auto_now_add=True)
    
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.title, allow_unicode=True)
        super(Project, self).save()
    
    @property
    def duration(self):
        
        end = self.end_time or jdatetime.date.today()
        return (end - self.start_time).days
    
    duration.fget.short_description = "مدت اجرا"
    