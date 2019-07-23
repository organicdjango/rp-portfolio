from django.urls import path
from . import views1

urlpatterns = [
    path("", views1.blog_index, name="blog_index"),
    path("<int:pk>/", views1.blog_detail, name="blog_detail"),
    path("<category>/", views1.blog_category, name="blog_category"),
]
