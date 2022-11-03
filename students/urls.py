from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path("",views.index,name= 'students'),
    path("blog",views.blog,name= 'blog'),
    path("about",views.about,name= 'about'),
    path("contact",views.contact,name= 'contact'),
    path("editors_about",views.editors_about,name= 'editors_about'),
    path("design_about",views.design_about,name= 'design_about'),
    path("departmenthead_about",views.departmenthead_about,name= 'departmenthead_about'),
    path("CMA_about",views.CMA_about,name= 'CMA_about'),
    path("technical_about",views.technical_about,name= 'technical_about')

]
