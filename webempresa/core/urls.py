from django.urls import path
from . import views

urlpatterns = [
    # Paths del core -- la genero del primero ejercicio, lo coloco aqui en el segundo punto
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),

    path("store/", views.store, name="store"),
    
    
    

]
