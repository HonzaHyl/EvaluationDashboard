from django.urls import path

from dashboard.views import load_file, index, select_file, statistics, graphs

# App name is used in templates to call specific view via url command
# For example: href="{% url 'dashboard:index' ...%}"
app_name = "dashboard"

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('graphs/', graphs.as_view(), name='graphs'),
    path('statistics/', statistics.as_view(), name="statistics"),
    path('load_file/', load_file.as_view(), name='load_file'),
    path('select_file/', select_file.as_view(), name='select_file')
]