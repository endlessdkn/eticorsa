from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class perfil(models.Model):
    UsuarioCliente = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario en el Sistema', null=True, blank=True)
    NombreCliente = models.CharField(verbose_name='Nombre del Cliente', max_length=150)
    Abreviatura = models.CharField(verbose_name='Abreviatura', max_length=10)
    imgPerfil = models.ImageField(verbose_name='Imagen del Perfil', upload_to='static/cliente/perfil', height_field=None, width_field=None, max_length=None, null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.Abreviatura, self.NombreCliente)

    class Meta:
        db_table = 'perfil'
        managed = True
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'