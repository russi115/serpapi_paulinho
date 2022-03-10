from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Scraper import views

router = routers.DefaultRouter()
router.register(r'datas', views.DataView, 'datas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
