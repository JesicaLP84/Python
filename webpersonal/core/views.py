from django.shortcuts import render, HttpResponse

# html_base = """
# <h1>Mi web personal</h1>
# <ul>
#     <li><a href="/">Portada</a></li>
#     <li><a href="/about-me">Acerca de</a></li>
#     <li><a href="/portfolio">Portfolio</a></li>
#     <li><a href="/contact">Contact</a></li>
# </ul>
# """
# Create your views here. -- CREAMOS LAS VISTAS QUE VAMOS HACER CON FUNCIONES, NO METEDOS
# def home(request):
#     return HttpResponse("<h1>Mi web Personal</h1><h2>Portada</h2>")

# def home(request):
#     return HttpResponse(html_base + """
#         <h2>Portada</h2>
#         <p>Esto es la portada</p>
#     """)

##AHORA HACEMOS TEMPLATES
def home(request):
    return render(request,'core/home.html')

def about(request):
    return render(request,'core/about.html')

def portfolio(request):
    return render(request,'core/portfolio.html')

def contact(request):
    return render(request,'core/contact.html')

#Este ejemplo lo explica para hacer un bucle y añadir mas cosas a la vista -- ESto es el backend
# def home(request):
#     html_response = "<h1>Mi web Personal</h1>"
#     for i in range(10):
#         html_response += "<h2>Portada</h2>"
#     return HttpResponse(html_response)

# def about(request):
#     return HttpResponse("<h1>Mi web Personal</h1><h2>Acerca de</h2><p>Me llamo Jessica y soy programadora</p>")

# def about(request):
#     return HttpResponse(html_base + """
#         <h2>Acerca de</h2>
#         <p>Me llamo Jessica y soy programadora.</p>
#     """)
    
    
# def portfolio(request):
#     return HttpResponse(html_base + """
#         <h2>Proyecto Inicial</h2>
#         <p>Este es mi primer proyecto con Django</p>
#     """)
    
# def contact(request):
#     return HttpResponse(html_base + """
#         <h2>Contacto</h2>
#         <h3>Descripción de contacto</h3>
#         <p>Este es mi contacto: 
#             <p>Telefono:+52 123 4567
#             <p>Dirección: 123456789
#             <p>Email: jessica@gmail.com
#         </p>
#     """)