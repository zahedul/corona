from django.urls import path, include
from job import views

app_name = 'job'

urlpatterns = [
    path('', views.index, name='index'),
    path('update_status/', views.update_status, name='update_status'),
]