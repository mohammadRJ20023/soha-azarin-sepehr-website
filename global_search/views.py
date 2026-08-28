from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from portfolio.models import Project
from Services.models import Service


def search(request):

    query = request.GET.get("q", "").strip()

    projects = Project.objects.all().order_by("-created_at")
    services = Service.objects.all()

    if query:
        projects = projects.filter(
            Q(title__icontains=query)
            | Q(project_type__icontains=query)
        )
        services = services.filter(
            Q(title__icontains=query)
            | Q(task__icontains=query)
        )

    paginator = Paginator(projects, 6)
    page_number = request.GET.get("page")
    object_list = paginator.get_page(page_number)
    
    
    context = {
        "search_query": query,
        "projects": object_list,
        
    }
    return render(request, "global_search/search.html", context)