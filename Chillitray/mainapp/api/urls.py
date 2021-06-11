from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.ApiHome.as_view() , name= "ApiHome"),
    path('update/<pk>', views.ApiUpdateView.as_view() , name= "ApiUpdate"),
    path('delete/<pk>', views.ApiDeleteView.as_view() , name= "ApiDelete"),
    path('users', views.UsersApi.as_view() , name= "UsersApi"),
]
