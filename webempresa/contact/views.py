from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import   EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    # print("Tipo de peticion: {}".format(request.method))
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos el correo y redireccionamos

            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                ": De {} <{}>\n\nEscribiço:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["jesicalopezgomez84@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #Si va OK, redirecciona a OK
                return redirect(reverse(contact)+"?ok")
            except:
                #Si algo no va OK, redirecciona a FAiL
                return redirect(reverse(contact)+"?fail")

    return render(request,'contact/contact.html', {'form': contact_form})