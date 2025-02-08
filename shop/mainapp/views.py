from django.shortcuts import render
from .models import Product

# to help load the template file
from django.template import loader

# to help return an http reponse to the user for any given request
from django.http import HttpResponse

# Create your views here.
def homeView(request):
    #Querying the DB and getting a collection of product class objects from the records
    products = Product.objects.all() # Select * from product;

    # Creating a context dictionary to be used to render the template with info
    context ={
        'product_list' : products # the key we create here, will be available as a variable in template design in 'home.html'
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context,request))


def aboutView(request):
    context={
        'name':"Krishna",
        'student':[
            "suraj",
            "shivani",
            "deepak"
        ],
        'slept':True
    }
    template = loader.get_template('about.html')
    return HttpResponse(template.render(context,request))

def contactView(request):
    context={

    }
    template = loader.get_template('contacts.html')
    return HttpResponse(template.render(context,request))

