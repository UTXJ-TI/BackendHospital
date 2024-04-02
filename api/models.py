from django.db import models

# Create your models here.
class nacimientos_bebes(models.Model):
	id_bebe = models.CharField(max_length=50)
	fecha_nacimiento = models.CharField(max_length=50)
	hora_nacimiento = models.CharField(max_length=50)
	lugar_nacimiento = models.CharField(max_length=150)
	peso = models.CharField(max_length=15)
	longitud = models.CharField(max_length=100)
	nombre_padre = models.CharField(max_length=50)
	nombre_madre = models.CharField(max_length=50)
	telefono_contacto = models.CharField(max_length=50)
	email_contacto = models.CharField(max_length=50)
	observaciones = models.CharField(max_length=50)
	tipo_nacimiento = models.CharField(max_length=50)
	frecuencia_cardiaca = models.CharField(max_length=50)
	temperatura = models.CharField(max_length=50)
	presion_arterial_sistolica = models.CharField(max_length=50)
	presion_arterial_diastolica = models.CharField(max_length=50)
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

#Tabla estudio de
class c_estudio(models.Model):
	d_nombre = models.CharField(max_length=50)
	d_descripcion = models.CharField(max_length=250)


class Estudio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)

class Cita(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    paciente_id = models.IntegerField()  # Se asume que esto es un ID de paciente
    medico_id = models.IntegerField()  # Se asume que esto es un ID de médico
    #tipo_estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE, related_name='citas')

class ResultadoEstudio(models.Model):
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=500)
    imagen = models.BinaryField()

class Consumible(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class c_registrosM(models.Model):
    #ID = models.CharField(max_length=30)
    Persona_ID = models.CharField(max_length=30)
    Personal_Medico_ID = models.CharField(max_length=30)
    Fecha_Creacion_Archivo = models.CharField(max_length=150)
    Fecha_Edicion_Archivo = models.CharField(max_length=150)
    def __str__(self):return self.ID
		
     
class seguimiento_pediatria(models.Model):
	id_pediatrico = models.CharField(max_length=50)
	id_paciente = models.CharField(max_length=50)
	fecha_seguimiento = models.CharField(max_length=50)
	edad_años = models.CharField(max_length=50)
	peso = models.CharField(max_length=50)
	longitud = models.CharField(max_length=50)
	perimetro_craneal = models.CharField(max_length=50)
	temperatura = models.CharField(max_length=50)
	frecuencia_respiratoria = models.CharField(max_length=50)
	frecuencia_cardiaca = models.CharField(max_length=50)
	presion_arterial_sistolica = models.CharField(max_length=50)
	presion_arterial_diastolica = models.CharField(max_length=50)
	vacunas_administradas = models.CharField(max_length=50)
	examenes_medicos_realizados = models.CharField(max_length=50)
	observaciones = models.CharField(max_length=50)
	#website = models.URLField(max_length=100)
	#foundation = models.PositiveIntegerField()
    #TextField(blanck=True)
	def __str__(self):
		return self.ro_nombre

class solicitud_organos_1(models.Model):
	solicitud_ID = models.AutoField(primary_key=True)
	paciente_ID = models.IntegerField()
	medico_ID = models.IntegerField()
	organo_ID = models.IntegerField()
 
	class prioridad_2(models.TextChoices):
		urgente = 'urgente' 
		alta = 'alta'
		moderada = 'moderada'
	prioridad = models.CharField( max_length = 255, choices=prioridad_2.choices)
 
	fecha_solicitud = models.DateTimeField()
	dias_espera = models.IntegerField()
 
	class estatus_paciente(models.TextChoices):
		Transplante_exitoso = 'Transplante exitoso'
		Recuperacion = 'Recuperacion'
		Pendiente = 'Pendiente'
	estatus = models.CharField(  max_length = 255, choices=estatus_paciente.choices)
 
	def __str__(self):
		return self.solicitud_ID
     
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
    ID_cita = models.CharField(max_length=100)
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

#FARMACIA

class c_dispensacion_medicamentos(models.Model):
    # di_ID = models.AutoField(primary_key=True)
    Personal_Medico_ID = models.CharField(max_length=15)
    Receta_ID = models.CharField(max_length=15)
    Fecha_Registro = models.DateTimeField(auto_now_add=True)
    Total_Medicamentos_Solicitados = models.IntegerField()
    Total_Medicamentos_Entregados = models.IntegerField()  

    
    class Estado(models.TextChoices):
        Abastecido = 'Abastecido'
        Parcialmente_Abastecido = 'Parcialmente abastecido'

    
    Estatus = models.CharField(max_length=23, choices=Estado.choices, default=Estado.Abastecido)

    def __str__(self):
        return str(self.Receta_ID)
    
class c_detalle_dispensacion(models.Model):
    Dispensacion_ID = models.CharField(max_length=15)
    Detalle_Receta_ID = models.CharField(max_length=15)
    Fecha_Entrega = models.DateTimeField(auto_now_add=True)  
    Cantidad_Entregada = models.IntegerField()  
    Precio_Unitario = models.DecimalField(max_digits=10, decimal_places=2)
    Precio_Total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return str(self.Dispensacion_ID)

class c_detalle_dispensacion_relacion(models.Model):
    Dispensacion_ID = models.CharField(max_length=15)
    Detalle_Dispensacion_ID = models.CharField(max_length=15)
    

    class Estado(models.TextChoices):
        Validado = 'Validado'
        No_Validado = 'No Validado'

    
    Estatus = models.CharField(max_length=15, choices=Estado.choices, default=Estado.Validado)

class c_lotes_medicamentos(models.Model):
    Descripcion = models.CharField(max_length=15)
    Cantidad = models.IntegerField()  
    Precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)  
    Fecha_solicitud = models.DateField() 
    Fecha_ingreso = models.DateField(auto_now_add=True) 
   
    def __str__(self):
        return str(self.Descripcion)

class c_detalle_lotes(models.Model):
    Lotes_ID = models.CharField(max_length=15)
    Codigo = models.CharField(max_length=15)
    Medicamento_ID = models.CharField(max_length=15)
    fecha_vencimiento = models.DateField() 
    Marca = models.CharField(max_length=50)  
    Precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)  
    Estatus = models.CharField(max_length=15)
   
    def __str__(self):
        return str(self.Lotes_ID)


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

class Puesto(models.Model):
    ID = models.AutoField(primary_key=True)
    # Departamento_ID = models.ForeignKey('Departamento', on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=100, null=False)
    Descripcion = models.TextField()
    Requisitos = models.TextField()
    Salario_Minimo = models.DecimalField(max_digits=10, decimal_places=2)
    Salario_Maximo = models.DecimalField(max_digits=10, decimal_places=2)
    Estatus = models.CharField(max_length=10, choices=(('activo', 'activo'), ('inactivo', 'inactivo')), default='activo')

    def __str__(self):
        return self.Nombre

class Horario(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, null=False)
    Descripcion = models.TextField()
    Tipo_Jornada = models.CharField(max_length=20, choices=(('diurna', 'diurna'), ('nocturna', 'nocturna'), ('turnos_rotativos', 'turnos_rotativos')), null=False)
    Dia_Laboral = models.CharField(max_length=50)
    Hora_Inicio = models.TimeField()
    Hora_Fin = models.TimeField()

    def __str__(self):
        return self.Nombre

class Personal(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, null=False)
    Genero = models.CharField(max_length=10, choices=(('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')), null=False)
    Fecha_Nacimiento = models.DateField(null=False)
    Direccion = models.CharField(max_length=255)
    Telefono = models.CharField(max_length=20)
    Correo_Electronico = models.CharField(max_length=100)
    #Puesto_ID = models.ForeignKey('Puesto', on_delete=models.CASCADE)
    #Horario_ID = models.ForeignKey('Horario', on_delete=models.CASCADE)
    Fecha_Inicio = models.DateField()
    Estatus = models.CharField(max_length=10, choices=(('activo', 'activo'), ('inactivo', 'inactivo')), default='activo')

    def __str__(self):
        return self.Nombre

    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    descripcion = models.TextField(max_length=150)
    salaOperaciones = models.TextField(max_length=150)
    tipoCirugia = models.TextField(max_length=150)
