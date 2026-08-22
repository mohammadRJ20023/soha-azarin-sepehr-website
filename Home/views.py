from django.shortcuts import render, redirect
from .forms import ContactUsForm
from .models import ContactUs
from portfolio.models import Project





def Home_page(request):
    
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
            
    projects = Project.objects.all()
    return render(request, "Home/Home.html", {"form":form, "projects":projects})


