from django.urls import path, include
#from . import views
app_name = 'users' # to distinguish from other possible apps
urlpatterns = [
    path('', include('django.contrib.auth.urls')), # adding specifi django authentication (take care lgoin log out)

]