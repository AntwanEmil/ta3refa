from django.urls import path
from . import views
urlpatterns =[
    path('', views.create_new_product , name='create_new_product'),
]