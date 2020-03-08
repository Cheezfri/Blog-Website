from django.urls import path
from . import views  # "." means current directory


urlpatterns = [
    path('', views.home, name='blog-home'),  # '' means empty homepage, view.home is the view that does logic
    path('about/', views.about, name='blog-about')
]