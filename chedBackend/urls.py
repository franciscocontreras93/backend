from django.conf.urls import url, re_path
from chedBackend import views


urlpatterns = [
    url(r'^api/tiendas$', views.tiendas_list),
    re_path(r'^api/tiendas/(?P<id_mg>[0-9]+)$', views.tiendas_detalle)
]

