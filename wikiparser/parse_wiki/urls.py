from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from parse_wiki import views


router = DefaultRouter()
router.register(r'', views.ArticleViewSet)


urlpatterns = [
    url(r'^article/', include(router.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
]
