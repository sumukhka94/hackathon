from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('chart/', views.chart,name='chart'),
    path('chart_view/',views.chart_view,name='chart_view'),
    path('chart_view/get_chart_data/', views.get_chart_data, name='get_chart_data'),
]