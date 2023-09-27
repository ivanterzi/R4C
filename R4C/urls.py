"""R4C URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
    1. Import the include() function: from django.urls import include, path
     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
 """
from django.contrib import admin
from django.urls import path


from django.contrib import admin
from django.urls import path, include
from robots import views
api = [
     path('create_robot/', views.create_robot, name='create_robot'),
     path('get_robots', views.get_robots, name = 'get_robots'),
 ]
urlpatterns = [
     path('admin/', admin.site.urls),
     path('api/', include(api)),

 ]