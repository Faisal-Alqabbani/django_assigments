from django.urls import path
from django.http import JsonResponse
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('blogs', views.index, name='blogs'),
    path('blogs/new',views.new),
    path('blogs/create', views.create),
    path('blogs/json', views.json),
    path('blogs/<int:number>', views.show),
    path('blogs/<int:number>/edit', views.edit),
    path('blogs/<int:number>/delete', views.delete),
   
]