# Apuntes del proyecto

1.- Las Vistas la generamos con HTTResponse en el primer ejercicio en archivo views-core y en urls-app

2.- Las urls de app la pasamos a un archivo nuevo de urls.py en core eliminandolas del archivo urls-app

3.- Crear los templeates y static en core para cargar con {% load static %} -- Detectar las partes comunes
    Cambiamos las vistas de HTTResponse a render

    Revisamos que partes de la base.html se elimina para añadir las de los demas templates, en home.html se deja solo cabecera y mensaje
    De la base cambiamos los enlaces del menu navegador {% url '' %}

    NOTA: descomprimo los tamplates que vienen en el curso para dejarlos en la carpeta de templates/core y los reviso para saber de que forman quedan.
    Comenzé al inicio del ejercio a tocar el de about.

4.- Colocar en los items del menu navegador para que con request.path podamos seleccionar y se sombree del color que tiene todos los elementos en cada url

5.- Crear la app Services:
    - Crear carpeta media y Colocar en settings     MEDIA_URL = '/media/'    MEDIA_ROOT = os.path.join(BASE_DIR, "media") ( importar os) directorio donde va a buscar
    - en url importar los settings y asi colocar un if para que el DEBUG de los archivos medias esten dirigidos con la ruta donde se encuentran

    - creamos la app services y creamos el modelo de servicio :

    -realizamos la migración completa (python manage.py makemigrations ), (python manage.py migrate ) --> con esto migramos todas las apps

    -COMANDO PARA CREAR SUPERUSUARIO:  python3 manage.py createsuperuser
                        Username (leave blank to use ’jesica.lopez’):

                        Email address: webempresa@webempresa.net

                        Password: ​1234hola

                        Password (again): 1234hola

    - Para acceder a admin : en el archivo admin-services importamos service de .models y creamos una configuracion  basica indicando los campos de lectura de created y updated,
    registramos el servicio y su configuracación

    - En settings configuramos el idioma de admin e indicamos el nuevo nombre de la app indicado en apps.services

    AÑADIR ESTA PARTE QUE ES EL DEL PUNTO ULTIMO QUE HE REALIZADO

5.- Crear la app blog para  las relaciones forengkin o manitomany .. para declarar varias instancias
    - Creamos la app blog y luego a models para crear los modelos . uno para categorias y otro para los pots
    APUNTE = tema de importar timezone.now con las migraciones indica siempre una incidencia. se cambia en from django.utils.timezone import now y por default = now para que asi quede que se muestre reflejada la fecha de publicación actual en la clase del modelo

    -- Cuando meto la publicación en admin, reviso el sitio y no me aparece publicaa, incluso poniendole la hora de ahora 

6.- Editar Admin en el blog:
    Para poder visualizar mas categorias en el servidor, añadimos la list_display

7.- Crear Vistas al Blog:
    Carpeta templates/blog creando el archivo views.blog