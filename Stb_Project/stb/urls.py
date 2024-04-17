from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('chart/', views.chart, name='chart'),
    path('about/', views.about, name='About-Us'),
    path('technical-analysis/', views.ta, name='technical-analysis'),
    path('fundamental-analysis/', views.fundamental, name='fundamental-analysis'),
]
