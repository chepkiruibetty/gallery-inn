from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import SearchResultsListView

urlpatterns=[
    path('',views.home,name='home'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('',views.search_location,name='search_location'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
