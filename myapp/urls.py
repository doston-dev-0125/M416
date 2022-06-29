from django.urls import path
from .views import login_page,signup,home,specifications,about,contact,order
urlpatterns = [
    path('',home,name='home'),
    path('specifications',specifications,name='specifications'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('signup',signup,name='signup'),
    path('login',login_page,name='login'),
    path('order_list',order,name='order')
]