from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage_view, name='home_page'),
    path('journals/', views.journals, name='journals'),
]
