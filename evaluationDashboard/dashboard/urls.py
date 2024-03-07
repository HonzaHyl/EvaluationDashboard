from django.urls import path

from . import views

# App name is used in templates to call specific view via url command
# For example: href="{% url 'dashboard:index' ...%}"
app_name = "dashboard"

urlpatterns = [
    path('', views.index, name='index'),
    path('genefamilies/', views.genefamilies, name='genefamilies'),
    path('load_file/', views.load_file, name='load_file'),
]