from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path('', views.postslist.as_view(), name='posts'),
    path('<slug:slug>/', views.postdetail.as_view(), name='post_detail'),
]
