from django.shortcuts import render
from django.views.generic import ListView

from .models import Images,Category,Location

# Create your views here.
class PhotosListView(ListView):
    model = Images
    template_name ='home.html'