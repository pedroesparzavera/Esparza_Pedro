from django.shortcuts import redirect, render
from Esparza_APP.models import Asistente
from Esparza_APP.forms import FormAsistente

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listarAsistente(request):
    asistente = Asistente.objects.all()
    data = {'asist': asistente}
    return render(request, 'listarAsistente.html', data)

def agregarAsistente(request):
    form = FormAsistente

    if request.method == 'POST' :
        form = FormAsistente(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    
    data = {'formP' : form}
    return render(request, 'agregarAsistente.html', data)


def eliminarAsistente(request, id):
    asist = Asistente.objects.get(id = id)
    asist.delete()
    return redirect('/listarP')

def actualizarAsistente(request, id):
    Asist = Asistente.objects.get(id = id)
    form = FormAsistente(instance=Asist)
    
    if request.method == 'POST':
        form = FormAsistente(request.POST, instance=Asist)
        if form.is_valid() :
            form.save()
        return index(request)
    
    data = {'formP' : form}
    return render(request, 'agregarAsistente.html', data)
