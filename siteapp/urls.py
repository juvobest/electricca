from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('' , views.index ,name="home"),
    path('about' , views.about ,name="about"),
    path('contact' , views.contact ,name="contact"),
    path('services' , views.services ,name="services"),
    path('testimonial' , views.testimonial ,name="testimonial"),

]