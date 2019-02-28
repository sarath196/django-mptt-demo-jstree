from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class RenderLanding(TemplateView):
    template_name = "landing.html"