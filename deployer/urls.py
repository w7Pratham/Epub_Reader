from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('home/',views.home, name='home'),
    path('upload/', views.upload_epub, name='upload_epub'),
    path('read/<int:epub_id>/', views.read_epub, name='read_epub'),
]
