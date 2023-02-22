from django.shortcuts import get_object_or_404, render, redirect
from directores_cine.forms import DirectorForm, PeliculaForm
from directores_cine.models import Director, Pelicula

# Create your views here.


def index(request):
    no_directores = Director.objects.count()
    no_peliculas = Pelicula.objects.count()
    return render(request, 'index.html', {'no_directores': no_directores, 'no_peliculas': no_peliculas, 'pagina': 'home', 'titulo': 'Home'})


def listar_directores(request):
    directores = Director.objects.all()
    return render(request, 'directores.html', {'directores': directores, 'pagina': 'directores', 'titulo': 'Listar Directores'})


def nuevo_director(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DirectorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('directores')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DirectorForm()

    return render(request, 'editar-director.html', {'form': form, 'pagina': 'directores', 'titulo': 'Nuevo Director', 'modo': 'crear'})


def editar_director(request, id):
    director = get_object_or_404(Director, pk=id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DirectorForm(request.POST, instance=director)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('directores')
    else:
        form = DirectorForm(instance=director)
    return render(request, 'editar-director.html', {'form': form, 'pagina': 'directores', 'titulo': 'Editar Director', 'modo': 'editar'})


def eliminar_director(request, id):
    director = get_object_or_404(Director, pk=id)
    if director:
        director.delete()
        return redirect('directores')


def listar_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas.html', {'peliculas': peliculas, 'pagina': 'peliculas', 'titulo': 'Listar Peliculas'})


def nueva_pelicula(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PeliculaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('peliculas')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PeliculaForm()

    return render(request, 'editar-pelicula.html', {'form': form, 'pagina': 'peliculas', 'titulo': 'Nueva Pelicula', 'modo': 'crear'})


def editar_pelicula(request, id):
    director = get_object_or_404(Pelicula, pk=id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PeliculaForm(request.POST, instance=director)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('peliculas')
    else:
        form = PeliculaForm(instance=director)
    return render(request, 'editar-pelicula.html', {'form': form, 'pagina': 'peliculas', 'titulo': 'Nueva pelicula', 'modo': 'editar'})


def eliminar_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, pk=id)
    if pelicula:
        pelicula.delete()
        return redirect('peliculas')
