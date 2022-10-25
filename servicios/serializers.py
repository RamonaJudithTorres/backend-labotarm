from rest_framework import serializers
from .models import *


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPaciente
        fields = '__all__'  

# CREAR PACIENTE
    def create(self, validated_data):
        nombre=validated_data.get('nombre','')
        edad=validated_data.get('edad','')
        telefono=validated_data.get('telefono','')

        paciente= ModelPaciente.objects.create(
        nombre=nombre,
        edad=edad,
        telefono=telefono,
        )
        return paciente 



# SERIALIZER ESTUDIO

class EstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelEstudio
        fields = '__all__'   

# CREAR ESTUDIO
    def create(self, validated_data):
        nombre=validated_data.get('nombre','')
        clave=validated_data.get('clave','')
        descripcion=validated_data.get('descripcion','')

        estudio= ModelEstudio.objects.create(
        nombre=nombre,
        clave=clave,
        descripcion=descripcion,
        )
        return estudio 


# SERIALIZER SERVICIOS

class CreateServicioSerializer(serializers.ModelSerializer):
    # paciente=PacienteSerializer()
    # estudio=EstudioSerializer(many=True)
    class Meta:
        model = ModelServicio   
        fields = '__all__'
      
    # CREAR SERVICIO
    def create(self, validated_data):
        costo=validated_data.get('costo','')
        clave=validated_data.get('clave','')
        resultado=validated_data.get('resultado','')
        paciente=validated_data.get('paciente','')
        estudio=validated_data.get('estudio','')
        print(validated_data)
        servicio= ModelServicio(
        costo=costo,
        clave=clave,
        resultado=resultado,
        paciente=paciente,
        # estudio=estudio,
        )
        servicio.save()
        for i in estudio:
            servicio.estudio.add(i)
        # servicio.save()
        return servicio




# SERIALIZER TARJETAS
class TarjetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjetas
        fields = '__all__'        


class ListServicioSerializer(serializers.ModelSerializer):
    paciente=PacienteSerializer()
    estudio=EstudioSerializer(many=True)
    class Meta:
        model = ModelServicio   
        fields = '__all__'
      
