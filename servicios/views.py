from django.shortcuts import get_object_or_404, render
from .serializers import *
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

# VISTA API PACIENTES
# READ
class ApiPaciente(APIView):
    def get (self, request,  paciente_id=None):
        pacientes = ModelPaciente.objects.all()
        page_number= request.query_params.get('page_number', 1)
        page_size=request.query_params.get('page_size', 10)
        filter_nombre = request.query_params.get('nombre', '')

        if  paciente_id:
            paciente=ModelPaciente.objects.get(id=paciente_id)
            paciente_serializer= PacienteSerializer(paciente)
            return Response({'data':paciente_serializer.data})

        else:    
            pacientes=ModelPaciente.objects.filter(nombre__icontains=filter_nombre)
            all_items = pacientes.count()

            paciente_paginator =Paginator(pacientes, per_page=page_size)
            paciente_serializer= PacienteSerializer (paciente_paginator.page(page_number), many=True)
            return Response(
                                {'data':paciente_serializer.data,
                                'all_items': all_items,
                                })

    #PACIENTES POST METHOD CREATE 
    def post(self,request):
        paciente_serializer= PacienteSerializer(data= request.data)

        if paciente_serializer.is_valid():
            paciente = paciente_serializer.save()
            return Response(
                 {'paciente_id':paciente.id,
                 'message': 'Paciente creado con éxito' })
        else:
            errors = paciente_serializer.errors
        return Response(
                        {'data':errors,
                        'message': 'Error al crear paciente' })





# VISTA API ESTUDIOS
# READ

class ApiEstudios(APIView):
    def get (self, request,  estudio_id=None):
        # estudios = ModelEstudio.objects.all()
        page_number= request.query_params.get('page_number', 1)
        page_size=request.query_params.get('page_size', 10)
        filter_nombre = request.query_params.get('nombre', '')
        filter_clave = request.query_params.get('clave', '')

        if  estudio_id:
            estudio=ModelEstudio.objects.get(id=estudio_id)
            estudio_serializer= EstudioSerializer(estudio)
            return Response({'data':estudio_serializer.data})

        else:    
            estudios = ModelEstudio.objects.filter(nombre__icontains=filter_nombre,
            clave__icontains=filter_clave,)
            all_items = estudios.count()

            estudio_paginator =Paginator(estudios, per_page=page_size)
            estudio_serializer= EstudioSerializer (estudio_paginator.page(page_number), many=True)
            return Response(
                                {'data':estudio_serializer.data,
                                'all_items': all_items,
                                })
    #PACIENTES POST METHOD CREATE 
    def post(self,request):
        estudio_serializer= EstudioSerializer(data= request.data)

        if estudio_serializer.is_valid():
            estudio = estudio_serializer.save()
            return Response(
                 {'estudio_id':estudio.id,
                 'message': 'Estudio creado con éxito' })
        else:
            errors = estudio_serializer.errors
        return Response(
                        {'data':errors,
                        'message': 'Error al crear Estudio' })



# VISTA API Servicios
# READ

class ApiServicios(APIView):
    def get (self, request,  servicio_id=None):
        servicios = ModelServicio.objects.all().order_by('-fecha')        
        page_number= request.query_params.get('page_number', 1)
        page_size=request.query_params.get('page_size', 10)
        filter_clave = request.query_params.get('clave', '')

        if  servicio_id:
            servicio=ModelServicio.objects.get(id=servicio_id)
            servicio_serializer= ListServicioSerializer(servicio)
            return Response({'data':servicio_serializer.data})

        else:    
            servicios = ModelServicio.objects.filter(
            clave__icontains=filter_clave,)
            all_items = servicios.count()

            servicio_paginator =Paginator(servicios, per_page=page_size)
            servicio_serializer= ListServicioSerializer (servicio_paginator.page(page_number), many=True)
            return Response(
                                {'data':servicio_serializer.data,
                                'all_items': all_items,
                                })          
    def post(self,request):
        servicio_serializer= CreateServicioSerializer(data= request.data) 
        if servicio_serializer.is_valid():
            servicio = servicio_serializer.save()
            return Response(
                 {'servicio_id':servicio.id,
                 'message': 'Servicio creado con éxito' })
        else:
            errors = servicio_serializer.errors
        return Response(
                        {'data':errors,
                        'message': 'Error al crear Servicio'})



# VISTA API TARJETAS
# READ

class ApiTarjetas(APIView):
    def get (self, request ):
        """ paginacion """
        page_number = request.query_params.get('page_number')
        page_size = request.query_params.get('page_size')
        
        tarjetas = Tarjetas.objects.all()

        tarjeta_paginator = Paginator(tarjetas, per_page=page_size)

        tarjetas_serializer= TarjetasSerializer (tarjeta_paginator.page(page_number), many=True)

        return Response({'data': tarjetas_serializer.data})                                              

