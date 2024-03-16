#http://127.0.0.1:8000/walkingdead

# urlpatterns = [
#     path("", views.home),
#     path("home", views.home),
# ]

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import hotel_image_view
 
urlpatterns = [
    path('detect-supernova', hotel_image_view, name='hotel_image_view'),
]
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
