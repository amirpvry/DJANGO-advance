from django.urls import path , include
from . import views


urlpatterns = [

    path('registration', views.RegesterationApiView.as_view(), name ='registration')
]



