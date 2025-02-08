from django.urls import path
from .views import homeView, aboutView, contactView # importing the views from the mainapp to access the function

urlpatterns =[
    path("",homeView, name='home'),
    path("about",aboutView,name='about'),
    path("contacts",contactView, name='contact')
]