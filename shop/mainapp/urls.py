from django.urls import path
from.import views # importing the views from the mainapp to access the function

urlpatterns =[
    path("", views.homeView, name='home')
]