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
    Se crae un archivo urls.py para definir la ruta
    En core elimino dicha ruta y vista para que solo se ejecute desde el template de blog
    El template se hace la fusion para que se pueda ver mi publicación desde admin cuando en entremos en server/blog/

        - Nota: no me salia la vista que yo creaba en admin por faltarme un S en {'posts': posts}

8.- Crear las vistas para entrar en las categorias de Ofertas y General:
        Hay que pasarle un campo dinamico para ello darle un ID en category
        Se crea en viwes y en url de blog, importante se le indica int:category_id para que salga un numero entero, no una cadena de caracteres
        en views se coloca get_object_or_404 para que nos muestre el error de que no encuentra un Id no generado en la DB
        en models colocamos related_name='get_posts' en categories para hacer la busqueda mas sencilla en la url de la web,
            además, en la instancia de category.html colocamos esto category.get_posts.all para buscar por todas las categorias
        modificamos el spam de blog.html y category.html para que siga apareciendo resaltado la tecla de menu de Blog y las categorias en la parte inferior

9.-Crear app Social
    en el modelo colocamos SlugField para utilizar caracteres alfanumericos
    Se genera toda la migracion y demás, configurando los archivos correspondientes que hemos realizado con las apps anteriores
    En Admin se meten las redes sociales con los enlaces de cada una menos la de instagram

10.-Crear un procesador de contexto:
    Generamos un archivo processors en social donde configuramos el contexto con los links
    en base.html creamos la fusion de cada enlace para que se vean y se reedirigan a las urls que hemos puesto en admin


11.-Crear la pagina Sample(page):
    creamos la apps page
    modificamos en models la clase meta para que se ordene por titulo y se muestro por ello, no por -created
    creamos en admin las paginas
    Tras modificar en admin las paginas, no me aparecen en la url como 1,2,3 ... cambia la id

12.- Crear paginas Extras
    Se crea carpeta templatestags y los archivos __init__.py y pages_extras.py
    Adaptando el archivo pages_extras con el decorador de la libreria de tags, cuando hago el cambio en el template base.html , no me aparece en la url la muestra de los querys en la parte de pie de pagina ... Reviso todo y no soy capaz de sacar que puede estar sucediendo.
        ESTO APARECE EN LA TERMINAL :     django.template.exceptions.TemplateSyntaxError: 'pages_extras' is not a registered tag library. Must be one of:
                                            admin_list
                                            admin_modify
                                            admin_urls
                                            cache
                                            i18n
                                            l10n
                                            log
                                            static
                                            tz

tras varias revisiones ,, comsigo que visualice ..


13.- Ordenar las paginas:
    En el modelo incluimos una variable order y tambien la indicamos en la prioridad dentro de ordering dentro de la clase Meta
    Hacemos la migración y ya en admin guardamo el numero de orden de prioridad para que se muestra en la web
    Crear enlace de Editar para acceder a admin y asi actulizar la pagina

14.- Editor Wayseewait -- CKEditor:
    django CKeditor se instala ( pip install django-ckeditor )
    en settings lo colocamos en apps instaladas
    en modelo de pages cambiamos la variable de contenido indicandole un RichTextField ademas de importar de la libreria ckeditor
    hacemos la migracion de nuevo para hacer los cambios
    Hemos incluido la barra de editar el texto del contenido

    añadiendo un diccionario CKEDITOR_CONFIGS -- para que sea mas extendido las posibilidades de ediccion de texto
        None es la mas extendido y Basic es la mas reducida

15.- Editar la vista de contacto con los formularios de la web:
    craremos la apps contact
    crear un diseño de formulario que ofrece django se crea dentro de la app como forms.py - -es parecido a crear el modelo
    Hay varias formas de darle forma en maquetación al formulario , finalmente dejamos
            <table>
            {{form.as_table}}
            </table>

16.- Crear el boton de enviar Formulario:
    Se toca el template para darle el imput del botón
    Hacemos la verificacion de cada campo y comprobar el dominio para que sea con TOKEN {%csrf token%}

17.- Proceso avanzado de darle forma al formulario
    EmailImput es para que indique el mensaje de que le falta el @
    se indica minimo y maximo que no aparece en el mensaje en el formulario --- REVISAR porque no lo explica

18.- Enviar Emails de prueba:
    Django tiene un modulo para enviar email
    configuramos una cuenta de correo y utilizamos la plataforma mailtrap
    me registro en mailtrap y copiamos estos datos en settigns:
    EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = '2525'

    en el archivo viwes se importa la libreria EmailMessage

    adaptamos el views con la clase para realizar la prueba de email a mailtrap --- Me sale todo OK y reviso mi mensaje en el servidor de mailtrap


19.- LIMITAR ACCESOS DEL CLIENTE EN ADMIN:
    usos de grupo u permisos de usarios