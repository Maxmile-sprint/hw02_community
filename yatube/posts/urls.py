from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Create a path function for main page

    path('', views.index, name='index'),

    # Create a path function for page of a certain group

    path('group/<slug:slug>/', views.group_posts, name='group_list')
]
