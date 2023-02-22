from django.contrib import admin
from django.urls import path
from vazifa_list.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',register_page, name='register_page'),
    path('login/',login_page,name='login'),
    path('create_task/',create_task,name='create_task'),
    path('logout_user/',logout_user,name='logout_user'),
    path('home_page/',home_page,name='home_page'),
    path('delete_task/<int:pk>/',delete_task, name='delete_task'),
    path('detail_page/',detail_page, name='detail_page'),
]

   
