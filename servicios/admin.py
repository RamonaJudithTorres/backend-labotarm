from django.contrib import admin
from .models import ModelPaciente, ModelServicio, ModelEstudio, Tarjetas
# Register your models here.

admin.site.register(ModelEstudio)
admin.site.register(ModelPaciente)
admin.site.register(ModelServicio)
admin.site.register(Tarjetas)