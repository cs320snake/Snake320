from django.urls import path, include
from django.contrib.auth.forms import UserCreationForm
from . import views
#from . import views
app_name = 'users' # to distinguish from other possible apps
urlpatterns = [
    path('', include('django.contrib.auth.urls')), # adding specifi django authentication (take care lgoin log out)
    path('register/', views.register, name='register')
]