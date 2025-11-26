from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class HomeView(View):
    def get(self, request):
        context = {
            'message': 'Welcome to the Home Page!'
        }
        return render(request, 'home.html', context);