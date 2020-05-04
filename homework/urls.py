from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', IndexView.as_view()),
]



