from django.contrib import admin

from jalali_date.admin import ModelAdminJalaliMixin

from .models import Project, CompanyStats

admin.site.register(CompanyStats)

@admin.register(Project)
class ProjectAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ("title","start_time", "end_time", "duration", "status")