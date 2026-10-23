from django.db import models

# Create your models here.

class AutoPkMixin(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk is None:
            last = self.__class__.objects.order_by('-id').first()
            self.id = (last.id + 1) if last else 1
        super().save(*args, **kwargs)


class Categoria(AutoPkMixin):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'categoria'

    def __str__(self):
        return '%s' % (self.nombre)


class Cliente(AutoPkMixin):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)


class Proveedor(AutoPkMixin):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'proveedor'

    def __str__(self):
        return '%s' % (self.nombre)


class Usuario(AutoPkMixin):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    user = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=45)
    rol = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return '%s' % (self.nombre)


class Producto(models.Model):
    nombre = models.CharField(max_length=45)
    precio_compra = models.FloatField(blank=True, null=True)
    precio_venta = models.FloatField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria')
    activo = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'producto'

    def __str__(self):
        return '%s' % (self.nombre)


class Compra(AutoPkMixin):
    id = models.IntegerField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    id_proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='id_proveedor')
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'compra'

    def __str__(self):
        return 'Compra %s' % (self.id)


class DetalleCompra(AutoPkMixin):
    id = models.IntegerField(primary_key=True)
    id_compra = models.ForeignKey(Compra, models.DO_NOTHING, db_column='id_compra')
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')
    cantidad = models.IntegerField(blank=True, null=True)
    precio_unitario = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_compra'

    def __str__(self):
        return 'Detalle %s' % (self.id)


class Venta(AutoPkMixin):
    id = models.IntegerField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_usuario = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'venta'

    def __str__(self):
        return 'Venta %s' % (self.id)


class DetalleVenta(AutoPkMixin):
    id = models.IntegerField(primary_key=True)
    id_venta = models.ForeignKey(Venta, models.DO_NOTHING, db_column='id_venta')
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')
    cantidad = models.IntegerField(blank=True, null=True)
    precio_unitario = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_venta'

    def __str__(self):
        return 'Detalle %s' % (self.id)
