from django.shortcuts import render
from .models import Product

# importing url resolution tools
from django.urls import reverse, reverse_lazy

# to help load the template file
from django.template import loader

# to help return an http reponse to the user for any given request
from django.http import HttpResponse

# importing the generic class based views for CRUD operations
from django.views.generic import CreateView,DetailView,UpdateView, DeleteView


# Create your views here.
def homeView(request):
    #Querying the DB and getting a collection of product class objects from the records
    products = Product.objects.all() # Select * from product;

    # Creating a context dictionary to be used to render the template with info
    context ={
        'product_list' : products, # the key we create here, will be available as a variable in template design in 'home.html'
        'current_page':'home' # 
    }

    template = loader.get_template('home.html')
    return HttpResponse(template.render(context,request))


def aboutView(request):
    context={
       'current_page':'about' 
    }
    template = loader.get_template('about.html')
    return HttpResponse(template.render(context,request))

def contactView(request):
    context={

    }
    template = loader.get_template('contacts.html')
    return HttpResponse(template.render(context,request))

# Views for adding, editing and deleting products CRUD


#Create
class AddProduct(CreateView):
    model=Product
    fields = ['name','price','desc','pic','stock']
    template_name='addproduct.html'
    success_url=reverse_lazy('home')

# Read -> show details of each product
class ProductDetails(DetailView):
    model=Product
    template_name ='prod_details.html'
    context_object_name='prod'

# update ->
class Updateproduct(UpdateView):
    model = Product
    fields ='__all__'
    template_name = 'editProduct.html'

    #Overriding a method to produce 
    def get_success_url(self):
        return reverse('prod_details',kwargs={'pk':self.object.pk})
    
# Delete
class DeleteProduct(DeleteView):
    model=Product
    template_name='delProduct.html'
    success_url=reverse_lazy('home')

# search result 
def searchView(request):
    query=request.GET.get('search_text')
    #fetch the query text from GET request

    result =Product.objects.filter(name_icontains=query)
    # collect the product objects matching the name
    # This runs 'SELECT * FROM product WHERE name like  '%<query>%';
    # icontains is case-insensitive

    context = {
        'items':result,
        'query':query
    }
    template = loader.get_template('searchResult.html')
    return HttpResponse(template.render(context,request))


