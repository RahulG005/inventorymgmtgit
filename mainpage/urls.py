from . import views
from django.urls import path, include


urlpatterns = [
    path('',views.main_page, name ='main_page'),
]