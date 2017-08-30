from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from parse_wiki import views


router = DefaultRouter()
router.register(r'', views.ArticleViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
