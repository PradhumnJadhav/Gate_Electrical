from django.urls import path
from . import views

urlpatterns = [
    path('', views.sayHelo, name='members'),
     path('resources/', views.resources, name='res'),
    
      path('resources/machines/', views.resources_machines, name='res'),
    path('resources/machines/lecture/', views.resources_machines_lecture, name='res_lect'),
     path('resources/power-systems/', views.resources_system_lecture, name='res_sys_lect'),
      path('resources/power-electronics/', views.resources_pe_lecture, name='res_sys_lect'),
    
]