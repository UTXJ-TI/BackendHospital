from django.db import models
from django.utils import timezone

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
		return self.id_paciente

class UnsignedIntAutoField(models.AutoField):
    def db_type(self, connection):
        if 'mysql' in connection.settings_dict['ENGINE']:
            return 'int UNSIGNED AUTO_INCREMENT'
        return 'int'

class UnsignedForeignKey(models.ForeignKey):
    def db_type(self, connection):
        if 'mysql' in connection.settings_dict['ENGINE']:
            return 'int UNSIGNED'
        return 'int'

class personas(models.Model):
    ID = UnsignedIntAutoField(primary_key=True)
    titulo = models.CharField(max_length=45, null=True)
    nombre = models.CharField(max_length=80)
    primer_apellido = models.CharField(max_length=80)
    segundo_apellido = models.CharField(max_length=80, null=True)
    curp = models.CharField(max_length=18, unique=True, null=True)
    class generoOpciones(models.TextChoices):
        M = 'M' 
        F = 'F'
        NB = 'N/B'
    genero = models.CharField(max_length=50, choices=generoOpciones.choices)
    class grupoSanguineoOpciones(models.TextChoices):
        A = 'A'
        B = 'B'
        AB = 'AB'
        O = 'O'
    grupo_sanguineo = models.CharField(max_length=50, choices=grupoSanguineoOpciones.choices)
    class tipoSanguineoOpciones(models.TextChoices):
        Positivo = '+' 
        Negativo = '-'
    tipo_sanguineo = models.CharField(max_length=50, choices=tipoSanguineoOpciones.choices)
    fecha_nacimiento = models.DateField()
    estatus = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(default=timezone.now)
    fecha_actualizacion = models.DateTimeField(null=True)

    def  __str__(self):
        return self.ID

class pacientes(models.Model):
    persona_ID = UnsignedForeignKey(personas, primary_key=True, on_delete=models.CASCADE, db_column='persona_ID')
    nss = models.CharField(max_length=15, null=True)
    tipo_seguro = models.CharField(max_length=50, null=True)
    fecha_registro = models.DateTimeField(default=timezone.now)
    fecha_ultima_cita = models.DateTimeField()
    estatus_medico = models.CharField(max_length=100, default='Normal', null=True)
    class estatusVidaOpciones(models.TextChoices):
        Vivo = 'Vivo'
        Finado = 'Finado'
        Coma = 'Coma'
        Vegetativo = 'Vegetativo'
    estatus_vida = models.CharField(max_length=50, choices=estatusVidaOpciones.choices, default='Vivo')
    estatus = models.BooleanField(null=True)

    def __str__(self):
        return self.persona_ID

class personal_medico(models.Model):
    persona_ID = UnsignedForeignKey(personas, primary_key=True, on_delete=models.CASCADE, db_column='persona_ID')
    especialidad = models.CharField(max_length=50, null=True)
    class tipoOpciones(models.TextChoices):
        Medico = 'Médico'
        Enfermero = 'Enfermero'
        Administrativo = 'Administrativo'
        Directivo = 'Directivo'
        Apoyo = 'Apoyo'
        Residente = 'Residente'
        Interno = 'Interno'
    tipo = models.CharField(max_length=50, choices=tipoOpciones.choices)
    cedula_profesional = models.CharField(max_length=50, unique=True, null=True)
    departamento_ID = models.PositiveIntegerField()
    class estatusOpciones(models.TextChoices):
        Activo = 'Activo'
        Inactivo = 'Inactivo'
        Jubilado = 'Jubilado'
        Permiso = 'Permiso'
    
    estatus = models.CharField(max_length=50, choices=estatusOpciones.choices)
    fecha_contratacion = models.DateTimeField(default=timezone.now)
    fecha_termino_contrato = models.DateTimeField(null=True)

    def __str__(self):
        return self.persona_ID

class organos(models.Model):    
    ID = UnsignedIntAutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    aparato_sistema = models.CharField(max_length=50)
    descripcion = models.TextField()
    detalle_organo_ID = models.PositiveIntegerField()
    estatus = models.BooleanField()

    def __str__(self):
        return self.ID

class solicitud_transplantes(models.Model):
    ID = UnsignedIntAutoField(primary_key=True)
    paciente_ID = UnsignedForeignKey(pacientes, on_delete=models.CASCADE, db_column='paciente_ID')
    medico_ID = UnsignedForeignKey(personal_medico, on_delete=models.CASCADE, db_column='medico_ID')
    organo_ID = UnsignedForeignKey(organos, on_delete=models.CASCADE, db_column='organo_ID')
 
    class prioridadOpciones(models.TextChoices):
       Urgente = 'Urgente' 
       Alta = 'Alta'
       Moderada = 'Moderada'
    prioridad = models.CharField( max_length = 50, choices=prioridadOpciones.choices)
 
    fecha_solicitud = models.DateTimeField()
    dias_espera = models.IntegerField()
 
    class estatusOpciones(models.TextChoices):
       Transplante_exitoso = 'Transplante exitoso'
       Recuperacion = 'Recuperacion'
       Pendiente = 'Pendiente'
    estatus = models.CharField(max_length = 50, choices=estatusOpciones.choices) 
    estatus_aprobacion = models.BooleanField(default=False)
    
    def __str__(self):
        return self.ID
     
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


# Modelo Farmacia Intrahospitalaria ------------------------------------------


class c_dispensacion_medicamentos(models.Model):
    # di_ID = models.AutoField(primary_key=True)
    di_Receta_ID = models.CharField(max_length=15)
    di_Personal_Medico_ID = models.CharField(max_length=15)
    di_Fecha_Registro = models.DateTimeField(auto_now_add=True)
    di_Total_Medicamentos_Solicitados = models.IntegerField()
    di_Total_Medicamentos_Entregados = models.IntegerField()  

    # Definir la enumeración para el campo de estado
    class Estado(models.TextChoices):
        DISPONIBLE = 'Disponible'
        NO_DISPONIBLE = 'No Disponible'

    # Agregar el campo de estado con las opciones de la enumeración
    di_estatus = models.CharField(max_length=15, choices=Estado.choices, default=Estado.DISPONIBLE)

    def __str__(self):
        return str(self.di_Receta_ID)

    


class c_detalles_dispensacion(models.Model):
    di_Dispensacion_ID = models.CharField(max_length=15)
    di_Detalle_Receta_ID = models.CharField(max_length=15)
    di_Fecha_Entrega = models.DateTimeField(auto_now_add=True)  
    di_Cantidad_Entregada = models.IntegerField()  
    di_Precio_Unitario = models.DecimalField(max_digits=10, decimal_places=2)
    di_Precio_Total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return str(self.di_Dispensacion_ID)



class c_lotes_medicamentos(models.Model):
    di_Medicamento_ID = models.CharField(max_length=15)
    di_Descripcion = models.CharField(max_length=15)
    di_Cantidad = models.IntegerField()  
    di_fecha_vencimiento = models.DateField() 
    di_fecha_ingreso = models.DateField(auto_now_add=True) 
   
    def __str__(self):
        return str(self.di_Medicamento_ID)

class c_detalle_lotes(models.Model):
    di_Lotes_ID = models.CharField(max_length=15)
    di_Codigo = models.CharField(max_length=15)
    di_Marca = models.CharField(max_length=50)  
    di_Precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)  
    di_Estatus = models.CharField(max_length=15)
   
    def __str__(self):
        return str(self.di_Lotes_ID)



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
        ('En Proceso', 'En Proceso'),
        ('Cancelado', 'Cancelado')
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


class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    area_medica = models.ForeignKey('AreaMedica', on_delete=models.SET_NULL, null=True, blank=True)
    departamento_superior = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    responsable = models.ForeignKey('PersonalMedico', on_delete=models.SET_NULL, null=True, blank=True, related_name='departamentos_responsable')
    estatus = models.IntegerField(default=1)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'departamentos'


class AreaMedica(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(null=True, blank=True)
    estatus = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'areas_medicas'


class Persona(models.Model):
    TITULO_CHOICES = [
        ('Sr.', 'Sr.'),
        ('Sra.', 'Sra.'),
        ('Srta.', 'Srta.'),
        ('Dr.', 'Dr.'),
        ('Dra.', 'Dra.'),
        ('Lic.', 'Lic.'),
        ('Ing.', 'Ing.'),
        ('Prof.', 'Prof.'),
        ('Otro', 'Otro'),
    ]
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('N/B', 'No binario'),
    ]
    GRUPO_SANGUINEO_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ]
    TIPO_SANGUINEO_CHOICES = [
        ('+', 'Positivo'),
        ('-', 'Negativo'),
    ]

    titulo = models.CharField(max_length=45, null=True, blank=True, choices=TITULO_CHOICES)
    nombre = models.CharField(max_length=80)
    primer_apellido = models.CharField(max_length=80)
    segundo_apellido = models.CharField(max_length=80, null=True, blank=True)
    curp = models.CharField(max_length=20, null=True, blank=True)
    genero = models.CharField(max_length=3, choices=GENERO_CHOICES)
    grupo_sanguineo = models.CharField(max_length=2, choices=GRUPO_SANGUINEO_CHOICES)
    tipo_sanguineo = models.CharField(max_length=1, choices=TIPO_SANGUINEO_CHOICES)
    fecha_nacimiento = models.DateField()
    estatus = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'personas'


class PersonalMedico(models.Model):
    TIPO_CHOICES = [
        ('Médico', 'Médico'),
        ('Enfermero', 'Enfermero'),
        ('Administrativo', 'Administrativo'),
        ('Directivo', 'Directivo'),
        ('Apoyo', 'Apoyo'),
        ('Residente', 'Residente'),
        ('Interno', 'Interno'),
    ]
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('Jubilado', 'Jubilado'),
        ('Permiso', 'Permiso'),
    ]

    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='personal_medico')
    especialidad = models.CharField(max_length=50, null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    cedula_profesional = models.PositiveIntegerField(null=True, blank=True)
    estatus = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Activo')
    fecha_contratacion = models.DateTimeField(auto_now_add=True)
    fecha_terminacion_contrato = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'personal_medico'


# --------------------Vistas de DG---------------------------------------------------------------

class VistaEstadoSolicitudes(models.Model):
    mes = models.IntegerField(primary_key=True)  # Utilizamos el mes como clave primaria
    num_aprobadas = models.IntegerField()
    num_en_proceso = models.IntegerField()
    num_no_aprobadas = models.IntegerField()
    num_canceladas = models.IntegerField()

    class Meta:
        managed = False  # Esto le dice a Django que esta tabla no será gestionada por él
        db_table = 'vista_estado_solicitudes'      

class VistaCantidadPersonalMedico(models.Model):
    medicos = models.IntegerField(primary_key=True) 
    enfermeros = models.IntegerField()
    administrativos = models.IntegerField()
    directivos = models.IntegerField()
    apoyo = models.IntegerField()
    residentes = models.IntegerField()
    internos = models.IntegerField()

    class Meta:
        managed = False  # Indica a Django que no gestione esta tabla (ya que es una vista de MySQL)
        db_table = 'vista_cantidad_personal_medico'  # Nombre de la vista en la base de datos

class VistaCantidadPacientes(models.Model):
    cantidad_total_personas = models.IntegerField(primary_key=True) 
    cantidad_femeninos = models.IntegerField()
    cantidad_masculinos = models.IntegerField()

    class Meta:
        managed = False  # Indica a Django que no gestione esta tabla (ya que es una vista de MySQL)
        db_table = 'vista_pacientes'  # Nombre de la vista en la base de datos

class VistaOperacionesBitacora(models.Model):
    inserciones = models.IntegerField(primary_key=True) 
    actualizaciones = models.IntegerField()
    eliminaciones = models.IntegerField()

    class Meta:
        managed = False  # Indica a Django que no gestione esta tabla (ya que es una vista de MySQL)
        db_table = 'vista_operaciones_bitacora'  # Nombre de la vista en la base de datos

# -----------------------------------------------------------------------------------

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
