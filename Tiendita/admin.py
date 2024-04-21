from django.contrib import admin
from .models import Region, Delivery, Empleado, Proveedor, Categoria, Producto, Formato, Cliente, Orden, Transaccion, Membresia, Servicio


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id_region', 'ciudad')
    search_fields = ('ciudad',)

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id_delivery', 'nombre_compania', 'telefono')
    search_fields = ('nombre_compania',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'nombre', 'titulo', 'ciudad', 'direccion', 'telefono', 'fecha_nacimiento')
    search_fields = ('nombre', 'titulo', 'ciudad')

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'nombre_compania', 'telefono', 'pais', 'ciudad', 'direccion')
    search_fields = ('nombre_compania', 'pais', 'ciudad')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'genero', 'descripcion')
    search_fields = ('genero', 'descripcion')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'proveedor', 'nombre_producto', 'tipo_producto', 'autor', 'unidades', 'precio', 'categoria')
    search_fields = ('nombre_producto', 'tipo_producto', 'autor', 'categoria__genero')

@admin.register(Formato)
class FormatoAdmin(admin.ModelAdmin):
    list_display = ('id_formato', 'producto', 'fisico', 'digital')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'telefono', 'region', 'direccion')
    search_fields = ('nombre', 'telefono', 'direccion', 'region__ciudad')

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id_orden', 'cliente', 'producto', 'delivery', 'empleado', 'ciudad', 'direccion', 'fecha_venta')
    search_fields = ('cliente__nombre', 'producto__nombre_producto', 'empleado__nombre')

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('id_transaccion', 'orden', 'producto', 'precio_producto', 'monto_total', 'metodo_pago')
    list_filter = ('metodo_pago',)
    search_fields = ['orden__id_orden', 'orden__cliente__nombre']

    def producto(self, obj):
        return obj.orden.producto.nombre_producto if obj.orden.producto else "No especificado"
    producto.short_description = 'Producto'

    def precio_producto(self, obj):
        return obj.orden.producto.precio if obj.orden.producto else 0
    precio_producto.short_description = 'Precio del Producto'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('orden__producto')  # Asegura que la orden y el producto se carguen junto con la transacción

    def orden_id(self, obj):
        return obj.orden.id_orden
    orden_id.short_description = 'ID de Orden'
    orden_id.admin_order_field = 'orden__id_orden'

    def save_model(self, request, obj, form, change):
        # Verificar si ya existe una transacción para esta orden
        existing_transactions = Transaccion.objects.filter(orden=obj.orden)
        if existing_transactions.exists():
            # Si ya existe una transacción para esta orden, no se guarda la nueva transacción
            return
        
        # Si no existe una transacción para esta orden, se guarda la nueva transacción
        super().save_model(request, obj, form, change)

@admin.register(Membresia)
class MembresiaAdmin(admin.ModelAdmin):
    list_display = ('id_membresia', 'cliente', 'tipo', 'fecha_inicio', 'fecha_fin', 'estado')
    search_fields = ('cliente__nombre', 'tipo', 'estado')
    list_filter = ('tipo', 'estado', 'fecha_inicio', 'fecha_fin')

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    search_fields = ('titulo',)

