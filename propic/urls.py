from django.urls import path
from .views import get_image,getallpics

app_name = 'propic'


urlpatterns = [
    path("get-image",get_image,name='getimage'),
    path("allpics",getallpics,name="allpics"),
]