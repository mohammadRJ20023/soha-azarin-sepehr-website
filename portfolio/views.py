from django.shortcuts import render, get_object_or_404
from .models import Project





def Project_detail(request, slug):
    
    # project = Project.objects.get(slug=slug) or:
    project = get_object_or_404(Project, slug=slug)

    return render(request, "Project_detail.html", {"project": project})