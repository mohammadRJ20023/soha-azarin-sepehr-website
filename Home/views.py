from django.shortcuts import render





def Home_page(request):
    
    return render(request, "Home/Home.html", {})


