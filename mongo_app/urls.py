from django.urls import path,include
from django.contrib import admin
from mongo_app import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
router.register(r'consulta_pacientes', views.PacienteAreaViewSet)
router.register(r'area_pacientes', views.PacientesConsultaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
	path('api_mongo/v1',include(router.urls)),
    path('docs/', include_docs_urls(title="hospital Mongo API'S")),
]