from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listviewdisplaydata', views.listviewdisplaydata),
    path('orgdashboard', views.orgdashboard),
    path('sectororgs/<int:sector_id>', views.sectororogs),
    path('sectororgs/<int:sector_id>/<str:org_name>', views.sectororogdebts),
]