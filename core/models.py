from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#criando uma tabela....vamos chamá-la de eventos -> com os campos:
#TÍTULO - DESCRIÇÃO - LOCAL DO EVENTO - DATA DO EVENTO - DATA CRIAÇÃO

class Evento(models.Model):                                             #criando a CLASSE evento
    objects = None
    titulo = models.CharField(max_length=100)                           #TÍTULO -> campo; CHARFIELD -> tipo do campo; MAX_LENGTH (limite de caracteres que ele vai ter) -> parâmetro do campo
    descricao = models.TextField(blank=True, null=True)                 #DESCRIÇÃO-> campo; parametro BLANK -> pode ser em branco e NULL, nulo
    data_evento = models.DateTimeField(verbose_name='Data do evento')   #DATETIMEFIELD -> campo de data e hora; não pode ser nulo automáticamente
    data_criacao = models.DateTimeField(auto_now=True)                  #igual...pra saber a data que o usuário inseriu esse evento no meu banco; esse 'dado' tem que ser automático...parametro AUTO_NOW
#essa tabela é do usuário...então bora criar o usuario
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)         #IMPORT from django.contrib.auth.models import User


#MIGRAR ESSA CLASSE PARA UMA TABELA MESMO; ESSA TABELA PARA MEU BANCO DE DADOS
#NO TERMINAL => PYTHON MANAGE.PY MAKEMIGRATIONS CORE; antes instalar em settings; acrecentar core em INSTALLED_APPS

#para minha tabela pura...do jeito que tá...sem que o progrma auto-arrume -> exigir que a tabela chame evento
#crio a classe Meta

    class Meta:
        db_table = 'evento'

#tratando o objeto
#usando a função STR

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')


