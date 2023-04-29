from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


def about(request):
    return render(request, 'about.html')
