from django.shortcuts import render, HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("Inicio")

# def about(request):
#     return HttpResponse("Historia")

# def services(request):
#     return HttpResponse("Servicios")

# def store(request):
#     return HttpResponse("Visítanos")

# def contact(request):
#     return HttpResponse("Contacto")

# def blog(request):
#     return HttpResponse("Blog")

# def sample(request):
#     return HttpResponse("Sample")

def home(request):
    return render(request,'core/home.html')

def about(request):
    return render(request,'core/about.html')



def store(request):
    return render(request,'core/store.html')

def contact(request):
    return render(request,'core/contact.html')

def blog(request):
    return render(request,'core/blog.html')

def sample(request):
    return render(request,'core/sample.html')