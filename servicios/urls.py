from django.urls import path
from .views import *

urlpatterns = [
    path('pacientes/all', ApiPaciente.as_view(), name='all_pacientes'),
    path('pacientes/detail/<int:paciente_id>/', ApiPaciente.as_view(), name='detail_pacientes'),
    path('pacientes/create/', ApiPaciente.as_view()),
    path('estudios/all', ApiEstudios.as_view(), name='all_estudios'),
    path('estudios/detail/<int:estudio_id>/', ApiEstudios.as_view(),name='detail_estudios'),
    path('estudios/create/', ApiEstudios.as_view()),
    path('all', ApiServicios.as_view(), name='all_servicios'),
     path('create', ApiServicios.as_view(), name='create_servicios'),
    path('detail/<int:servicio_id>/', ApiServicios.as_view(),name='detail_servicios'),
    path('tarjetas', ApiTarjetas.as_view(), name='tarjetas'),
    # path('update/<int:product_id>/', ApiProduct.as_view()),
    # path('delete/<int:product_id>/', ApiProduct.as_view())
]