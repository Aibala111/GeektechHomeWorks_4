
from django.contrib import admin
from django.urls import path
from setting.views import goodbye,time
urlpatterns = [
    path('admin/', admin.site.urls),
    path('goodbye/',goodbye),
    path('time/',time),
]
