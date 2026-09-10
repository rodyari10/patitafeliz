from django.shortcuts import render, get_object_or_404, redirect
from .models import Mascota
from adopciones.forms import SolicitudForm

def inicio(request):
    return render(request, 'inicio.html')

def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'lista_mascotas.html', {'mascotas': mascotas})

def detalle_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    return render(request, 'detalle_mascota.html', {'mascota': mascota})

def nosotros(request):
    return render(request, 'nosotros.html')

def adoptar(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()  # Esto guarda los datos en la base de datos
            return redirect('gracias')  # Redirige a la página de gracias
    else:
        form = SolicitudForm()
    return render(request, 'adoptar.html', {'form': form})

def gracias(request):
    return render(request, 'gracias.html')
