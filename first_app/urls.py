from django.urls import re_path  # Use re_path instead of url (deprecated)
from first_app import views

urlpatterns = [
    re_path(r'^task$', views.taskApi),  
    re_path(r'^task/([0-9]+)$', views.taskApi), 
]
