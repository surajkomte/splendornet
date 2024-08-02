from django.urls import path
from . import views

urlpatterns=[
    path("hv/",views.homeView),
    path("av/",views.addview),
    path("sv/",views.showView)
]