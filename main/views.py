from django.shortcuts import render, redirect
from . import models
# Create your views here.


def home(request):
    context = {
        "about": models.AboutMe.objects.all()[0],
        "portfolios": models.Portfolio.objects.all(),
        "articles": models.Articles.objects.all(),
        "portcats": models.PortFolioCategory.objects.all(),
        "services": models.Services.objects.all(),
        "skills": models.Skills.objects.all(),
        "servicecats": models.ServiceCategory.objects.all(),
        "tests": models.Testimonials.objects.all(),
        "seo": models.Seo.objects.all()[0],
    }
    return render(request, 'index.html', context)





def article_details(request, id):
    obj = models.Articles.objects.get(id=id)
    context = {
        "obj":obj,
    }
    return render(request, 'details.html', context)



def project_details(request, id):
    obj = models.Portfolio.objects.get(id=id)
    context = {
        "obj":obj,
    }

    return render(request, 'details.html', context)




def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('name')
        message = request.POST.get('name')
        models.Contact(name=name, email=email, message=message).save()
    return redirect("home")
