from django.contrib import admin
from django.urls import path
from user.views.home import Index
from user.views.home import Signup
from .views.home import Login,logout,Contact

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('contact', Contact.as_view() , name='contact'),
]
