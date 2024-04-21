from django.db import models
from django.db.models import UniqueConstraint

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.ciudad

class Delivery(models.Model):
    id_delivery = models.AutoField(primary_key=True)
    nombre_compania = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre_compania

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_compania = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre_compania

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.genero

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=100)
    tipo_producto = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    unidades = models.PositiveIntegerField()
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre_producto

class Formato(models.Model):
    id_formato = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fisico = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    ciudad = models.CharField(max_length=100)
    direccion = models.TextField()
    fecha_venta = models.DateField()

    def __str__(self):
        return f"Orden {self.id_orden} - {self.cliente.nombre}"

class Transaccion(models.Model):
    id_transaccion = models.AutoField(primary_key=True)
    orden = models.ForeignKey('Orden', on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    metodo_pago = models.CharField(max_length=100)
    estado_pago = models.CharField(max_length=50)  # Por ejemplo, asumiendo que estado_pago es un CharField

    def __str__(self):
        return f"Transacción {self.id_transaccion}"

    class Meta:
        constraints = [
            UniqueConstraint(fields=['orden'], name='unique_order_transaction')
        ]


class Membresia(models.Model):
    id_membresia = models.AutoField(primary_key=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=100)

    def __str__(self):
        return f"Membresía {self.id_membresia}"

from django.db import models

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo
    