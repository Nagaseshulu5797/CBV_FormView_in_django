from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.views.generic import FormView
from app.forms import *
class CBN_form(FormView):
    template_name='CBN_form.html'
    form_class=SchoolForm

    def form_valid(self, form):
        form.save()
        return HttpResponse('Data is inserted successfully')
