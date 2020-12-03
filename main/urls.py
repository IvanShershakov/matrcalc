from django.urls import path
from . import views


urlpatterns = [
    path('', views.calc, name='calc'),
    path('instruction', views.instruction, name='instruction'),
    path('about', views.about, name='about'),
    path('set_size', views.set_size, name='set_size'),
    path('input_data', views.input_data, name='input_data'),
]
