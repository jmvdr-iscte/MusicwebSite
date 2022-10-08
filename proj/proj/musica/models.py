from django.db import models
from django.utils import timezone
from six import string_types
import datetime
from django.contrib.auth.models import User

class Utilizador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True, default=None)
    instrumento = models.CharField(max_length=10)
    estilo = models.CharField(max_length=10)
    iniciante = models.BooleanField(default=False)

class Post(models.Model):
    user = models.ForeignKey(User, db_constraint= False, on_delete=models.CASCADE, default = None)
    post_texto = models.CharField(max_length=1000)
    pub_data = models.DateTimeField('data de publicacao')
    imagem = models.CharField(max_length=1000, default = None, null=True)
    gosto = models.IntegerField(default=0)
    def incgosto(self):
        self.gosto= self.gosto+1
    def __str__(self):
        return self.post_texto
    def foi_publicada_recentemente(self):
        return self.pub_data >= timezone.now() - datetime.timedelta(days=1)

class Like(models.Model):
    user = models.ForeignKey(User, db_constraint= False, on_delete=models.CASCADE, default = None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default = None)

class Comentario(models.Model):
    user = models.ForeignKey(User, db_constraint= False, on_delete=models.CASCADE, default = None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comentario_texto= models.CharField(max_length=1000)
    pub_data= models.DateTimeField('data de publicacao')
    def __str__(self):
        return self.comentario_texto

class Pedido(models.Model):
    user = models.ForeignKey(User, db_constraint= False, on_delete=models.CASCADE, default = None)
    pedido_titulo = models.CharField(max_length=40, default=None)
    pedido_texto = models.CharField(max_length=1000, default=None)
    pedido_contacto = models.CharField(max_length=50, default=None)
    imagem = models.CharField(max_length=1000, default = None, null=True)
    pub_data= models.DateTimeField('data de publicação')
    def __str__(self):
        return self.pedido_assunto, self.pedido_texto, self.pedido_contacto

class Oferta(models.Model):
    user = models.ForeignKey(User, db_constraint= False, on_delete=models.CASCADE, default = None)
    oferta_titulo = models.CharField(max_length=40, default=None)
    oferta_texto = models.CharField(max_length=1000, default=None, null= True)
    oferta_contacto = models.CharField(max_length=50, default=None)
    pub_data= models.DateTimeField('data de publicação')
    def __str__(self):
        return self.oferta_assunto, self.oferta_texto, self.oferta_contacto

class Projeto(models.Model):
    user = models.ForeignKey(User, db_constraint= False, on_delete=models.CASCADE, default = None)
    projeto_titulo = models.CharField(max_length=40, default=None)
    projeto_texto = models.CharField(max_length=1000, default=None)
    projeto_contacto = models.CharField(max_length=50, default=None)
    projeto_instrumento = models.CharField(max_length=10, default=None)
    imagem = models.CharField(max_length=1000, default = None, null=True)
    pub_data= models.DateTimeField('data de publicação')
    def __str__(self):
        return self.projeto_titulo, self.projeto_texto, self.projeto_contacto, self.projeto_instrumento

class Vendas(models.Model):
    user = models.ForeignKey(User, db_constraint= False, on_delete=models.CASCADE, default = None)
    venda_titulo = models.CharField(max_length=40, default=None)
    venda_texto = models.CharField(max_length=1000, default=None)
    venda_contacto = models.CharField(max_length=50, default=None)
    venda_negociavel = models.BooleanField(default=False)
    venda_preco = models.FloatField(max_length=8, default=None)
    imagem = models.CharField(max_length=1000, default = None, null=True)
    pub_data = models.DateTimeField('data de publicação')
    def __str__(self):
        return self.venda_titulo, self.venda_texto, self.venda_contacto, self.venda_negociavel
