from django.urls import path

from recipes.views import home

# HTTP request

# return HTTP response


urlpatterns = [
    path('', home),
]
