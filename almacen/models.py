from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class Papel(models.Model):
    NombrePapel = models.CharField(verbose_name='Nombre del Papel', max_length=50)
    Presentacion = models.CharField(verbose_name='Presentacion del Papel', max_length=50)
    PzasPresentacion = models.SmallIntegerField(verbose_name='Piezas por presentacion', blank=True, null=True)
    Gramaje = models.CharField(verbose_name='Gramaje del Papel', max_length=250)

    def __str__(self):
        return '{} -{}' .format (self.NombrePapel, self.Gramaje)

    class Meta:
        db_table = 'Papel'
        managed = True
        verbose_name = 'Papel'
        verbose_name_plural = 'Papeles'

class Tinta(models.Model):
    NombreTinta = models.CharField(verbose_name='Nombre Color', max_length=250)
    Color = ColorField(default='#FF0000')
    Pantone = models.CharField(verbose_name='Codigo Pantone', max_length=50)
    Formula = models.CharField(verbose_name='Formula del Color', max_length=250, blank=True, null=True)

    def __str__(self):
        return '{} - {} ' .format(self.NombreTinta, self.Pantone)

    class Meta:
        db_table = 'Tinta'
        managed = True
        verbose_name = 'Tinta'
        verbose_name_plural = 'Tintas'

class Barniz(models.Model):
    Cobertura =(
        ('Registro', 'A Registro'),
        ('Base', 'Base'),
    )
    NombreBarniz = models.CharField(verbose_name='Nombre del Barniz', max_length=50)
    TipoCobertura = models.CharField(verbose_name='Tipo de Cobertura', choices=Cobertura, max_length=50)
    DescripcionBarniz = models.TextField(verbose_name='Descripcion del Barniz', blank=True, null=True)

    def __str__(self):
        return '{} - {}' .format(self.NombreBarniz, self.TipoCobertura)

    class Meta:
        db_table = 'Barniz'
        managed = True
        verbose_name = 'Barniz'
        verbose_name_plural = 'Barnices'

class Suaje(models.Model):
    Tipo_Suaje = (
        ('C','Colgante'),
        ('A','Adherible'),
        ('T','Tallera'),
        ('V','Vampiro'),
        ('B','Botonera'),
        ('G','Corte Guillotina'),
    )
    NumSuaje = models.CharField(verbose_name='Numero del Suaje', max_length=5)
    TipoSuaje = models.CharField(verbose_name='Tipo de Suaje', choices=Tipo_Suaje, max_length=5)
    NomSuaje = models.CharField(verbose_name='Nombre del Suaje', max_length=50)
    MedidaEtiqueta = models.CharField(verbose_name='Medida de la Etiqueta', max_length=50)
    MedidaPapel = models.CharField(verbose_name='Medida del Papel', max_length=50)
    CantEtiqueta = models.SmallIntegerField(verbose_name='Piezas en Suaje')

    def __str__(self):
        return '{}-{} {} con {} pzas' .format(self.NumSuaje, self.TipoSuaje, self.NomSuaje, self.CantEtiqueta)

    class Meta:
        db_table = 'Suaje'
        managed = True
        verbose_name = 'Suaje'
        verbose_name_plural = 'Suajes'

class Clisse(models.Model):
    NombreClisse = models.CharField(verbose_name='Nombre del Clisse', max_length=75)
    ImgClisse = models.ImageField(verbose_name='Imagen del Clisse', upload_to='static/desing/clisse', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.NombreClisse

    class Meta:
        db_table = 'Clisse'
        managed = True
        verbose_name = 'Clisse'
        verbose_name_plural = 'Clisses'

class Laser(models.Model):
    Tipo_Acabado =(
        ('Corte','Corte'),
        ('Grabado','Grabado'),
    )
    NombreLaser = models.CharField(verbose_name='Nombre del Acabado Laser', max_length=75)
    TipoLaser = models.CharField(verbose_name='Tipo de Acabado', choices=Tipo_Acabado, max_length=15)
    ImgLaser = models.ImageField(verbose_name='Imagen del Clisse', upload_to='static/desing/laser', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return '{} {}' .format(self.NombreLaser, self.TipoLaser)

    class Meta:
        db_table = 'Laser'
        managed = True
        verbose_name = 'laser'
        verbose_name_plural = 'laser'

class Foil(models.Model):
    NombreFoil = models.CharField(verbose_name='Codigo del Foil', max_length=75)
    ColorFoil = models.CharField(verbose_name='Color del Foil', max_length=75)
    AcabadoFoil = models.CharField(verbose_name='Acabado del Foil', max_length=275, blank=True, null=True)
    PresentacionFoil = models.CharField(verbose_name='Presentacion del Foil', max_length=250)

    def __str__(self):
        return '{} {} {}' .format(self.NombreFoil, self.ColorFoil, self.AcabadoFoil)

    class Meta:
        db_table = 'Foil'
        managed = True
        verbose_name = 'Foil'
        verbose_name_plural = 'Foils'

class Laminado(models.Model):
    NombreLaminado = models.CharField(verbose_name='Nombre del Laminado', max_length=75)
    AcabadoLaminado = models.CharField(verbose_name='Tipo de Laminado', max_length=125)
    DescripcionLaminado = models.CharField(verbose_name='Descriptcion del Laminado', max_length=275, blank=True, null=True)
    AnchoLaminado = models.CharField(verbose_name='Ancho del Laminado', max_length=275)
    PresentacionLaminado = models.CharField(verbose_name='Presentacion del Laminado', max_length=275)

    def __str__(self):
        return self.NombreLaminado

    class Meta:
        db_table = 'Laminado'
        managed = True
        verbose_name = 'Laminado'
        verbose_name_plural = 'Laminados'