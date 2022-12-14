from django.db import models

# Create your models here.
class Empresa(models.Model):
    NomEmpresa = models.CharField(verbose_name='Nombre de la Empresa', max_length=50)
    ImgEmpresa = models.ImageField(verbose_name='Imagen de la Empresa', upload_to='static/empresa/', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.NomEmpresa

    class Meta:
        db_table = 'empresa'
        managed = True
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'