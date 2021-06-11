from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Task2Api.as_view(),name="Task2API"),
    path('update/<pk>', views.Tast2ApiUpdateView.as_view(),name="Task2APIUpdate"),
    path('delete/<pk>',views.Task2ApiDeleteView.as_view(),name="Task2APIDelete"),
]
