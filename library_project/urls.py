from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.http import HttpResponse

def home(request):
    return HttpResponse("Library API is running")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('library.urls')),
    path('api-token-auth/', obtain_auth_token),
]