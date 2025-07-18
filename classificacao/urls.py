from django.urls import path
from .views import upload_file
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Página de aplicação funcionando !!")

urlpatterns = [
    path('', home_view),
]




