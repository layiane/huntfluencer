from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('huntapp/', include('huntapp.urls')),
    path('admin/', admin.site.urls),
]