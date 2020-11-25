from django.urls import path, include
from . import views
app_name = 'game' # to distinguish from other possible apps
urlpatterns = [
    path('', views.home, name= 'home'), # adding specifi django authentication (take care lgoin log out)
]