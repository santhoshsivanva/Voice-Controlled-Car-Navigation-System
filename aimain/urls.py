from django.urls import path
from . import views
from django.conf.urls import handler404


urlpatterns = [path("",views.index,name="views"),
path("manual/",views.manual,name="manual"),
path("automated/",views.automatedMode,name="auto"),
path("locationloaded/",views.check,name="check"),
path("Path/",views.map,name="map"),

]
