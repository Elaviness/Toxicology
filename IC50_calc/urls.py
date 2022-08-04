from django.urls import path
from .views import *

urlpatterns = [
    path('', about, name='main_page'),
    path('base/', base, name='base_page'),
    path('about/', about, name='about_page'),
    path('calc/', calc, name='calc_page'),
]
