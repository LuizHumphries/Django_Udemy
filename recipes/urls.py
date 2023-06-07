from django.urls import path

from recipes.views import contato, home, sobre

# HTTP request

# return HTTP response


urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato)
]
