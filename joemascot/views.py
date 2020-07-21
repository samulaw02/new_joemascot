from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.


class Home_View(TemplateView):
    template_name = 'client/home.html'
    success_url = reverse_lazy('home')


class Service_View(TemplateView):
    template_name = 'client/service.html'
    success_url = reverse_lazy('service')


class Contact_View(TemplateView):
    template_name = 'client/contact.html'
    success_url = reverse_lazy('service')


class About_View(TemplateView):
    template_name = 'client/about.html'
    success_url = reverse_lazy('service')
