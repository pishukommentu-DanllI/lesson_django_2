from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('error', views.error),
    re_path(r'^user/(?P<login>\D+)/(?P<name_folder>\D+)/(?P<number>\d+)', views.folders),
    re_path(r'^user/(?P<login>\D+)/(?P<name_folder>\D+)', views.folders),
    re_path(r'^user/(?P<login>\D+)', views.folders),
    re_path(f'^user', views.folders)
]