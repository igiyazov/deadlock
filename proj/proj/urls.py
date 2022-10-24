from django.contrib import admin
from django.urls import path

from bill.views import transfer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transfer/', transfer),
]
