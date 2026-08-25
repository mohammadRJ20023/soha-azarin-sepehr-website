from django.shortcuts import render, redirect
from .forms import ContactUsForm 
from .models import ContactUs, CompanyStats, TeamMember
from portfolio.models import Project
from Services.models import Service, ExecutiveUnit





def Home_page(request):
    
    if request.method == "GET":
        executive_units = ExecutiveUnit.objects.all()
        selected_unit = request.GET.get("unit")
        
        if selected_unit:
            services = Service.objects.filter(executive_unit=selected_unit)
        else:
            services = Service.objects.all()
        

    
    if request.method == "POST":
        
        form = ContactUsForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            text = form.cleaned_data.get("text")
            
            ContactUs.objects.create(name=name, email=email, text=text)
            
            form.save()

            return redirect("Home:Home")
    else:
        form = ContactUsForm    
            
    projects = Project.objects.all().order_by("-created_at")[:3]
    
    company_stats = CompanyStats.objects.all()
    team_member = TeamMember.objects.all()
    
    context = {
        "form":form,
        "projects":projects,
        "company_stats": company_stats,
        "team_member":team_member,
        "services" : services,
        "executive_units":executive_units
    }
    return render(request, "Home/Home.html", context)


    
