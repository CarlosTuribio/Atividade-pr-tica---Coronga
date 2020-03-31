from django.contrib import admin
from .models import Pessoa
from .models import Departamento
from .models import Carro
from .models import Solicita
from .models import Atende

# Register your models here.
@admin.register(Pessoa, Departamento, Carro,Solicita, Atende)
class PessoaAdmin(admin.ModelAdmin):
	pass
class DepartamentoAdmin(admin.ModelAdmin):
	pass
class CarroAdmin(admin.ModelAdmin):
	pass
class SolicitaAdmin(admin.ModelAdmin):
	pass
class AtendeAdmin(admin.ModelAdmin):
	pass