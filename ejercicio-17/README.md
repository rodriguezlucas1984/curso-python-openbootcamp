# Ejercicio

En este ejercicio tendrás que crear una aplicación en Django que almacene datos de directores de cine y luego se puedan ver sus películas, así como una descripción de las mismas.

Tienes que personalizar el admin de la aplicación y a su vez crear las vistas de cada una de las partes de la aplicación.

## Correr aplicación con pipenv

1.  Instalar entorno virtual y dependecias:
    `pipenv install`
2.  Generar un shell con el entorno virtual activado:
    `pipenv shell`
3.  Crear migraciones:
    `python manage.py makemigrations`
4.  Aplicar migraciones:
    `python manage.py migrate`
5.  Cargar datos de prueba(opcional):

    - directores:`python manage.py loaddata seed\directores.json`
    - peliculas `python manage.py loaddata seed\peliculas.json`

6.  Correr servidor de desarrollo:
    `python manage.py runserver`

Por defecto la aplicación es servida en : http://127.0.0.1:8000/

Para finalizar la ejecución del servidor de desarrollo presionar: ctrl+c.

Para cerrar el shell con el entorno virtual ingresar:
`exit`
