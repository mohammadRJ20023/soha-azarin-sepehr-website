from django.shortcuts import render, get_object_or_404
from .models import Project
from django.views.generic import ListView





def Project_detail(request, slug):
    
    # project = Project.objects.get(slug=slug) or:
    project = get_object_or_404(Project, slug=slug)
    

    return render(request, "portfolio/Project_detail.html", {"project": project})


class ProjectList(ListView):
    
    model = Project
    template_name = "portfolio/Project_list.html"
    paginate_by = 2 
    context_object_name = "project_list"
    queryset = Project.objects.all()