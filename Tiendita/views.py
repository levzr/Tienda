from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from Tiendita.models import Servicio
from  Tiendita.forms import FormularioContacto
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from .models import Producto
from carro.carro import Carro

def inicio(request):

    carro=Carro(request)


    return render(request, "Tiendita/inicio.html")

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "Tiendita/servicios.html", {"servicios": servicios})

def tienda(request):

    productos=Producto.objects.all()

    return render(request, "Tiendita/tienda.html",{"productos":productos})

def contacto(request):
    formularioC = FormularioContacto()

    if request.method == "POST":
        formularioC = FormularioContacto(data=request.POST)
        if formularioC.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            mensaje = "El usuario con nombre {} y la dirección {} escribe lo siguiente:\n\n{}".format(nombre, email, contenido)
            email = EmailMessage("Mensaje desde app django", mensaje, "", ["jesemolina8@gmail.com"], reply_to=[email])

            try:
                # Intenta enviar el correo electrónico
                email.send()
                return redirect(reverse('contacto') + '?valido')
            except Exception as e:
                # En caso de error, redirige con un parámetro de consulta 'novalido'
                print("Error al enviar el correo electrónico:", e)
                return redirect(reverse('contacto') + '?novalido')

    return render(request, "Tiendita/contacto.html", {"formularioC": formularioC})