from django.urls import path
from .views import homeView, aboutView, contactView,AddProduct,ProductDetails,Updateproduct,DeleteProduct,searchView # importing the views from the mainapp to access the function
#
urlpatterns =[
    path("",homeView, name='home'),
    path("about",aboutView,name='about'),
    path("contacts",contactView, name='contact'),

    path('Products/<int:pk>',      ProductDetails.as_view(),  name='prod_details'),#C
    path('products/add',           AddProduct.as_view(),      name='add_prod'),#R
    path('products/edit/<int:pk>', Updateproduct.as_view(),   name='edit_prod'),#U
    path('products/del/<int:pk>',  DeleteProduct.as_view(),   name='del_prod'),#D

    #Search path
    path('products/search',searchView,name='search')
    
]