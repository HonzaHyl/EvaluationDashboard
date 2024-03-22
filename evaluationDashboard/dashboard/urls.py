from django.urls import path

from . import views

# App name is used in templates to call specific view via url command
# For example: href="{% url 'dashboard:index' ...%}"
app_name = "dashboard"

urlpatterns = [
    path('', views.index, name='index'),
    path('graphs/', views.graphs, name='graphs'),
    path('statistics/', views.statistics, name="statistics"),
    path('load_file/', views.load_file, name='load_file'),
]