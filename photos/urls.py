from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('',views.search_image,name='search_image'),
    path('',views.categories,name='categories')
    
]