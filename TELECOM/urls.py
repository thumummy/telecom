
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('inner/', views.inner, name='inner'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('dropdown/', views.dropdowd, name='dropdown'),
    path('add/', views.add, name='add'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
    path('edit/<int:id>', views.edit),
    path('pay/', views.pay, name='pay'),
    path('token/', views.token, name='token'),
    path('stk/', views.stk, name='stk'),

]


