from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:blog_id>', detail, name ="detail"),
    path('new/', new, name = "new"),
    path('create/', create, name = "create"),
    path('edit/<str:blog_id>', edit, name = "edit"),
    path('update/<str:blog_id>', update, name = "update"),
    path('delete/<str:blog_id>', delete, name = "delete")
]