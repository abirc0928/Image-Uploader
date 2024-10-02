from django.urls import path,include
from .views import *
urlpatterns = [
    path('', img_upload, name='img_upload'),
    path('delete/<int:id>', delete_image, name='delete_image'),
]
