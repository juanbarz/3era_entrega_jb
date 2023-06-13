from django.shortcuts import render, redirect
from .models import Categoria, Noticia, Comentario
from .forms import NoticiaForm, BusquedaForm

def index(request):
    noticias = Noticia.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'index.html', {'noticias': noticias, 'categorias': categorias})

def agregar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoticiaForm()
    return render(request, 'agregar_noticia.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            noticias = Noticia.objects.filter(titulo__icontains=termino_busqueda)
            return render(request, 'resultados_busqueda.html', {'noticias': noticias, 'termino_busqueda': termino_busqueda})
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})
