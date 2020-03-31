from django.contrib.auth.models import User
from django.db import models

class Pessoa(models.Model):
	nome = models.CharField('Nome', max_length=128, blank=True, null=True)
	email = models.EmailField('E-mail', blank=True, null=True)
	

	class Meta:
		verbose_name='Usuario'
		verbose_name_plural='Usuários'

	def __str__(self):
		return self.nome

class Departamento(models.Model):
	nome = models.CharField('Nome', max_length=128, blank=True, null=True)
	responsavel = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

	class Meta:
		verbose_name='Departamento'
		verbose_name_plural='Departamentos'

	def __str__(self):
		return self.nome

class Carro(models.Model):
	nome = models.CharField('Nome', max_length=128, blank=True, null=True)

	class Meta:
		verbose_name='Carro'
		verbose_name_plural='Carros'

	def __str__(self):
		return self.nome

class Solicita(models.Model):
	Solicitante = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
	data = models.DateField(blank=True, null=True)
	hora = models.TimeField(blank=True, null=True)
	origem = models.CharField('Origem', max_length=128, blank=True, null=True)
	destino = models.CharField('Destino', max_length=128, blank=True, null=True)

	class Meta:
		verbose_name='Solicitar Transporte'
		verbose_name_plural='Solicitar Transportes'

	def __str__(self):
		return self.destino

class Atende(models.Model):
	solicitante = models.ForeignKey(Solicita, on_delete=models.CASCADE)
	carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
	Motorista = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
	
	class Meta:
		verbose_name='Atender Solicitação'
		verbose_name_plural='Atender Solicitações'

