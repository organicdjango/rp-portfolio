from django.urls import path
from hello_world import views


from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),

    # By default
    #path('', views.index, name='index'),
]