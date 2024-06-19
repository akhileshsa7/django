"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("emp/",views.emp_reg),
    path('stu',views.stdindex),
    path('uplo/',views.tech_add),
    path('set',views.setsession),
    path('get',views.getsession),
    path('del',views.delsession),
    path('cset',views.setcook),
    path('cget',views.getcook),
    path('crdd/',views.crud2),
    path('crdv/',views.crud1),
    path('crddl/<int:datakey>',views.crud3),
    path('crde/<int:de>',views.crud4),
    path('crdu/<int:d>',views.crud5),
    path("w1/",views.workhome),
    path('w2/',views.worklogin),
    path('w3/',views.edit),
    path('w4/',views.edit1),
]
