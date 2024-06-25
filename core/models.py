from django.db import models

# Create your models here.

class pedidos(models.Model):
    numero = models.IntegerField(null=False, primary_key=True)
    observacoes = models.CharField(max_length=255, null=True)
    dataRecebimento = models.DateField(verbose_name=None)
    dataEntrega = models.DateField(verbose_name=None, null=True)

    class Meta:
        db_table = 'pedidos'

class produtos(models.Model):
    id = models.AutoField(primary_key=True)
    peca = models.TextField(max_length=100, null=False)
    cor = models.TextField(max_length=20, null=True)
    qtd = models.IntegerField(null=False)
    pedido = models.ManyToManyField(pedidos)

    class Meta:
        db_table = 'produtos'
