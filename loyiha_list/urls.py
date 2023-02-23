from django.urls import path
from loyiha_list.views import *

urlpatterns = [
    path('',index_page, name='index_page'),
    path('about_page',about_page, name='about_page'),
    path('admission_page',admission_page, name='admission_page'),
    path('why_page',why_us_page, name='why_us_page'),
    path('contact',contact_page, name='contact_page'),
]
