from django.urls import path
from .views import *

urlpatterns = [
    path("blogpost/", get_post, name='get_post'),
    path("blogpost/<int:pk>", get_individual_post, name='get_individual_post'),
    path("blogpost/update/<int:pk>", update_post, name='update_post'),
    path("blogpost/delete/<int:pk>", delete_post, name='delete_post'),
    path("blogpost/create", create_post, name='create_post')
]