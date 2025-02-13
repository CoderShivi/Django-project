from django.urls import path
from .views import UserRegister, Login

urlpatterns = [
      path('login',Login.as_view(),name ='signin'),
      path('register',UserRegister.as_view(),name ='signup')
]

