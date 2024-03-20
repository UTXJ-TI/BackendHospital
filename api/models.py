from django.db import models

class c_cliente(models.Model):
	d_nombre = models.CharField(max_length=50)
	d_apellidoPaterno = models.CharField(max_length=50)
	d_apellidoMaterno = models.CharField(max_length=50)
	d_direccion = models.CharField(max_length=150)
	d_telefono = models.CharField(max_length=15)
	d_correo = models.CharField(max_length=100)
	d_contrasena = models.CharField(max_length=50)
	#website = models.URLField(max_length=100)
	#foundation = models.PositiveIntegerField()
    #TextField(blanck=True)
	def __str__(self):
		return self.d_nombre
	
class c_rol(models.Model):
	ro_nombre = models.CharField(max_length=50)
	#website = models.URLField(max_length=100)
	#foundation = models.PositiveIntegerField()
    #TextField(blanck=True)
	def __str__(self):
		return self.ro_nombre

class c_cirugia(models.Model):
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    edad = models.IntegerField()
    historial_medico = models.TextField()
    tipo_cirugia = models.CharField(max_length=100)
    medico = models.CharField(max_length=100)
    fecha_y_hora = models.DateTimeField()

    def __str__(self):
        return f'{self.nombre} {self.apellido1} {self.apellido2}'
	

class c_Solicitud_Cirugias(models.Model):
    ID_cita = models.CharField(max_length=100, unique=True)
    ID_paciente = models.CharField(max_length=100)
    ID_medico = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField()
    sala_de_operaciones = models.CharField(max_length=100)

    def __str__(self):
        return f'Cita: {self.ID_cita}, Paciente: {self.ID_paciente}, Medico: {self.ID_medico}'

		
    d_nombre = models.CharField(max_length=50)
    d_apellidoPaterno = models.CharField(max_length=50)
    d_apellidoMaterno = models.CharField(max_length=50)
    d_direccion = models.CharField(max_length=150)
    d_telefono = models.CharField(max_length=15)
    d_correo = models.CharField(max_length=100)
    d_contrasena = models.CharField(max_length=50)

    def __str__(self):
        return self.d_nombre

class c_receta_medica(models.Model):
    r_id = models.AutoField(primary_key=True)
    r_cita_id = models.CharField(max_length=15)
    r_fecha_hora_registro = models.CharField(max_length=15)
    r_estatus = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.r_id)

class c_receta_medica_detalles(models.Model):
    rc_id = models.AutoField(primary_key=True)
    rc_recetaId = models.CharField(max_length=15)
    rc_medicamento = models.CharField(max_length=15)
    rc_dosis = models.CharField(max_length=15)
    rc_solicitados = models.CharField(max_length=15)
    rc_precio = models.CharField(max_length=15)
    rc_fecha_venta = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.rc_id)

class c_inventario(models.Model):
    i_id = models.AutoField(primary_key=True)
    i_codigo = models.CharField(max_length=15)
    i_tipo_presentacion = models.CharField(max_length=15)
    i_via_administracion = models.CharField(max_length=15)
    i_cantidad = models.CharField(max_length=15)
    i_precio_costo = models.FloatField(default=0)
    i_precio_venta = models.FloatField(default=0)
    i_numero_lote = models.CharField(max_length=15)
    i_fecha_caducidad = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.i_id)


class c_dispensacion(models.Model):
    di_id = models.AutoField(primary_key=True)
    di_recetaId = models.CharField(max_length=15)
    di_medicamento = models.CharField(max_length=15)
    di_dosis = models.CharField(max_length=15)
    di_solicitados = models.CharField(max_length=15)
    di_cantidad = models.CharField(max_length=100)  # Cambiado a CharField con longitud más pequeña
    di_precio = models.CharField(max_length=15)
    di_fecha_venta = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.di_id)

	# Modelos de Direccion General ------------------

class ServiciosMedicos(models.Model):
    id = models.AutoField(primary_key=True)
    clave = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    departamento_id = models.IntegerField()
    instalacion_superior_id = models.IntegerField()
    estatus = models.CharField(max_length=20, choices=(
        ('Activa', 'Activa'),
        ('Mantenimeinto', 'Mantenimeinto'),
        ('Fuera de Servicio', 'Fuera de Servicio'),
        ('Suspendida', 'Suspendida')
    ))
    
class ServiciosHospitalarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=(
        ('Médico', 'Médico'),
        ('Administrativo', 'Administrativo')
    ))
    tipo_intervencion = models.CharField(max_length=22, choices=(
        ('Cirugia', 'Cirugia'),
        ('Servicio de Emergencia', 'Servicio de Emergencia'),
        ('Hospitalización', 'Hospitalización'),
        ('Consulta Externa', 'Consulta Externa'),
        ('Servicio Maternidad', 'Servicio Maternidad'),
        ('Laboratorio', 'Laboratorio'),
        ('Palitativos', 'Palitativos'),
        ('Rehabilitacion', 'Rehabilitacion'),
        ('Psiquiatria', 'Psiquiatria'),
        ('Farmacia', 'Farmacia'),
        ('Traslados', 'Traslados')
    ))
    descripcion = models.TextField()
    departamento_responsable_id = models.IntegerField()
    estatus = models.BooleanField(default=True)



class AprobacionesServicios(models.Model):
    id = models.AutoField(primary_key=True)
    servicio_paciente_id = models.IntegerField()
    departamento_solicitante = models.IntegerField()
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estatus = models.CharField(max_length=20, choices=(
        ('Aprobado', 'Aprobado'),
        ('No Aprobado', 'No Aprobado'),
        ('En Proceso', 'En Proceso')
    ), default='En Proceso')
    comentarios = models.TextField()
    fecha_aprobacion = models.DateTimeField(null=True)

    class Meta:
        verbose_name_plural = 'Aprobaciones de Servicios'


class BitacoraDG(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_tabla = models.CharField(max_length=80)
    usuario = models.CharField(max_length=80)
    operacion = models.CharField(max_length=10, choices=(
        ('Insert', 'Insert'),
        ('Update', 'Update'),
        ('Delete', 'Delete')
    ))
    descripcion = models.TextField()
    fecha_hora = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Bitácora DG'

class CalendarioCirugia(models.Model):
	#c_cliente = models.ForeignKey(c_cliente, on_delete=models.CASCADE)
    nombreMedico = models.TextField(max_length=100)
    #cirujano = models.ForeignKey(Cirujano, on_delete=models.CASCADE)
    #sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    descripcion = models.TextField(max_length=150)
    salaOperaciones = models.TextField(max_length=150)
    tipoCirugia = models.TextField(max_length=150)
