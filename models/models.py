# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Especialidad(models.Model):
    _name = 'neuroeduka.especialidad'
    _rec_name = 'nombre_e'

    nombre_e = fields.Char(string='Nombre Especialidad', size=50, required=True)
    especialista_ids = fields.One2many(
        comodel_name='neuroeduka.especialista', inverse_name='especialidad_id', string='Especialista', required=True)

class Especialista(models.Model):
    _name = 'neuroeduka.especialista'
    _rec_name = 'nombre_es'

    nombre_es = fields.Char(string='Nombre', size=50, required=True)
    rut_es = fields.Char(string='Rut', size=10, required= True)

    especialidad_id = fields.Many2one(
        comodel_name='neuroeduka.especialidad', inverse_name='especialista_id', required=True)  
    reserva_ids = fields.One2many('neuroeduka.reserva','especialista_id')
    consulta_ids = fields.One2many('neuroeduka.consulta','especialista_id')
    boleta_pago_ids = fields.One2many(
       comodel_name='neuroeduka.boleta_pago', inverse_name='especialista_id',string='Boletas', required=True)
    evolucion_ids = fields.One2many(comodel_name='neuroeduka.evolucion', inverse_name='especialista_id',string='Evolución', required=True)

      
class Box(models.Model):
    _name = 'neuroeduka.box'
    _rec_name = 'nombre_box'

    nombre_box = fields.Char(string='Nombre', size=50, required=True)
    detalle_box = fields.Text(string='Detalle')
    reserva_ids = fields.One2many('neuroeduka.reserva','box_id') 
 

class Paciente(models.Model):
    _name = 'neuroeduka.paciente'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', size=50, required=True)
    rut = fields.Char(string='Rut', size=10, required=True)
    fecha_nac = fields.Date(string='Fecha de Nacimiento', required=True)
    email = fields.Char(string='Correo Electronico', size=50, required=True)
    celular = fields.Char(string='Celular', size=9, required=True)
    det_prevision = fields.Selection([('fonasa', 'Fonasa'), ('isapre', 'Isapre'), (
        'particular', 'Particular')], string='Previsión', required=True)
    acompanante = fields.Char(string='Acompañante', size=50, required=True)
    escolaridad = fields.Char(string='Escolaridad', size=50, required=True)
    establecimiento = fields.Char(string='Establecimiento Educacional', size=50, required=True)
    nombre_edi = fields.Char(string='Nombre Edi. Prof.', size=50, required=True)
    derivado = fields.Char(string='Derivado por', size=50, required=True)

    terapia_ids = fields.One2many('neuroeduka.terapia','paciente_id')
    familiar_ids = fields.One2many(
        comodel_name='neuroeduka.familiar', inverse_name='paciente_id',string='Familiares', required=True)
    reserva_ids = fields.One2many(comodel_name='neuroeduka.reserva', inverse_name='paciente_id', string='Reservas', required=True)
    consulta_ids = fields.One2many(comodel_name='neuroeduka.consulta', inverse_name='paciente_id',string='Consultas', required=True)
    diagnostico_ids = fields.One2many(comodel_name='neuroeduka.diagnostico', inverse_name='paciente_id',string='Diagnósticos', required=True)
    tratamiento_ids = fields.One2many(comodel_name='neuroeduka.tratamiento', inverse_name='paciente_id',string='Tratamientos', required=True)
    boleta_pago_ids = fields.One2many(comodel_name='neuroeduka.boleta_pago', inverse_name='paciente_id',string='Boletas', required=True)
    evolucion_ids = fields.One2many(comodel_name='neuroeduka.evolucion', inverse_name='paciente_id',string='Evolución', required=True)
    dato_anamnesico_ids = fields.One2many('neuroeduka.dato_anamnesico','paciente_id')

class Terapia(models.Model):
    _name = 'neuroeduka.terapia'
    _rec_name = 'nombre_t'

    nombre_t = fields.Char(string='Nombre Terapeuta', size=50, required=True)
    profesion = fields.Char(string='Profesión', size=50, required=True)
    desde_c = fields.Char(string='Desde cuando', size=50, required=True)
    donde_a = fields.Char(string='Donde atiende', size=50, required=True)

    paciente_id = fields.Many2one(comodel_name='neuroeduka.paciente',
                                  inverse_name='terapia_id', required=True)
    
class Parentesco(models.Model):
    _name = 'neuroeduka.parentesco'
    _rec_name = 'nombre_parentesco'

    nombre_parentesco = fields.Char(string='Parentesco', size=50, required=True)
    familiar_ids = fields.One2many(
        comodel_name='neuroeduka.familiar', inverse_name='parentesco_id',string='Familiares', required=True)


class Familiar(models.Model):
    _name = 'neuroeduka.familiar'
    _rec_name = 'nombre_familiar'

    nombre_familiar = fields.Char(string='Nombre del Familiar', size=50, required=True)
    edad = fields.Char(string='Edad', size=50, required=True)
    ocupacion = fields.Text(string='Ocupación', required=True)
    paciente_id = fields.Many2one(comodel_name='neuroeduka.paciente',
                                  inverse_name='familiar_id', required=True)
    parentesco_id = fields.Many2one(comodel_name='neuroeduka.parentesco',
                                  inverse_name='familiar_id', required=True)

class Tratamiento(models.Model):
    _name = 'neuroeduka.tratamiento'
    _rec_name = 'descripcion_trat'

    descripcion_trat = fields.Text(string='Tratamiento', size=50, required=True)
    plan_apoyo = fields.Text(string='Plan de Apoyo', size=50, required=True)
    proximo_control = fields.Text(string='Próximo Control', required=True)
    paciente_id = fields.Many2one(comodel_name='neuroeduka.paciente', string='Paciente',
                                required=True)
    consulta_id = fields.Many2one(comodel_name='neuroeduka.consulta', string='Consulta',
                                 required=True)

class Reserva(models.Model):
    _name = 'neuroeduka.reserva'
    _rec_name = 'fecha'
  
    fecha = fields.Datetime(string="Fecha y Hora", required=True)
    estado = fields.Selection(
        [('pendiente', 'Pendiente'), ('realizada', 'Realizada')], string='Estado del Pago', required=True)   
    paciente_id = fields.Many2one(
        comodel_name='neuroeduka.paciente', string='Paciente', required=True)
    especialista_id = fields.Many2one(
        comodel_name='neuroeduka.especialista', string='Especialista', required=True)
    box_id = fields.Many2one(
        comodel_name='neuroeduka.box', string='Box', required=True)
    motivo_consulta_id = fields.Many2one(
        comodel_name='neuroeduka.motivo_consulta', string='Motivo de Consulta', required=True)


class Motivo_consulta(models.Model):
    _name = 'neuroeduka.motivo_consulta'
    _rec_name = 'nombre_motivo'

    nombre_motivo = fields.Char(string='Motivo de la consulta', size=50, required=True)
    precio = fields.Integer(string='Precio', required=True)
    reserva_ids = fields.One2many(
        comodel_name='neuroeduka.reserva', inverse_name='motivo_consulta_id',string='Reservas', required=True)
    consulta_ids = fields.One2many(
        comodel_name='neuroeduka.consulta', inverse_name='motivo_consulta_id',string='Consultas', required=True)
    boleta_pago_ids = fields.One2many(
        comodel_name='neuroeduka.boleta_pago', inverse_name='motivo_consulta_id',string='Boleta', required=True)
    
class Diagnostico(models.Model):
    _name = 'neuroeduka.diagnostico'
    _rec_name = 'descripcion_diagno'

    descripcion_diagno = fields.Text(string='Descripción del Diagnóstico', size=50, required=True)
   
    paciente_id=fields.Many2one(comodel_name='neuroeduka.paciente', string='Paciente', required=True)
    consulta_id=fields.Many2one(comodel_name='neuroeduka.consulta', string='Consulta', required=True)            

class Consulta(models.Model):
    _name = 'neuroeduka.consulta'
    _rec_name = 'fecha'

    fecha = fields.Datetime(string="Fecha y Hora", required=True)
    quien_consulta = fields.Char(string="Quién Consulta", required=True)
    descripcion = fields.Text(string="Descripción", required=True)
    paciente_id = fields.Many2one(
        comodel_name='neuroeduka.paciente', string='Paciente', required=True)
    especialista_id = fields.Many2one(
        comodel_name='neuroeduka.especialista', string='Especialista', required=True)
    motivo_consulta_id = fields.Many2one(
        comodel_name='neuroeduka.motivo_consulta', string='Motivo de la Consulta', required=True)
    tratamiento_ids = fields.One2many(comodel_name='neuroeduka.tratamiento', inverse_name='consulta_id', string='Tratamientos', required=True)
    diagnostico_ids = fields.One2many(comodel_name='neuroeduka.diagnostico', inverse_name='consulta_id', string='Diagnósticos', required=True)

class Administrador(models.Model):
    _name = 'neuroeduka.administrador'
    _rec_name = 'nombre_admi'

    nombre_admi = fields.Char(string='Nombre', size=50, required=True)
    rut_admi = fields.Char(string='Rut', size=10, required= True)
    celular = fields.Char(string='Celular', size=9, required=True)
    email = fields.Char(string='Correo Electronico', size=50, required=True)
    factura_ids = fields.One2many('neuroeduka.factura','administrador_id')

class Proveedor(models.Model):
    _name = 'neuroeduka.proveedor'
    _rec_name = 'nombre_proveedor'

    nombre_proveedor = fields.Char(string='Nombre Proveedor', size=50, required=True)
    rut = fields.Char(string='Rut', size=10, required=True)
    razon_social = fields.Char(string='Razón Social', size=50, required=True)
    tipo_proveedor = fields.Selection([('fijo', 'Fijo'), ('variable', 'Variable')], string='Tipo de Proveedor', required=True)

    producto_ids = fields.One2many(
        comodel_name='neuroeduka.producto', inverse_name='proveedor_id',string='Producto', required=True)

class Producto(models.Model):
    _name = 'neuroeduka.producto'
    _rec_name = 'nombre_producto'

    nombre_producto = fields.Char(string='Nombre Producto', size=50, required=True)
    caracteristica = fields.Char(string='Características', size=10, required=True)
    unidad_medida = fields.Char(string='Unidad de Medida', size=50, required=True)

    detalle_factura_ids = fields.One2many(
       comodel_name='neuroeduka.detalle_factura', inverse_name='producto_id',string='Detalle de Factura', required=True)
    proveedor_id=fields.Many2one(comodel_name='neuroeduka.proveedor', string='Proveedor', required=True)

class Detalle_Factura(models.Model):
    _name = 'neuroeduka.detalle_factura'
    _rec_name = 'precio_unitario'

    precio_unitario = fields.Integer(string='Precio Unitario', size=50, required=True)
    cantidad = fields.Integer(string='Cantidad', size=10, required=True)
    producto_id=fields.Many2one(comodel_name='neuroeduka.producto', string='Producto', required=True)
    factura_id=fields.Many2one(comodel_name='neuroeduka.factura', string='Factura', required=True)

class Factura(models.Model):
    _name = 'neuroeduka.factura'
    _rec_name = 'num_factura'

    num_factura= fields.Integer(string='Número de Factura', size=50, required=True)
    monto_total = fields.Integer(string='Monto Total', size=50, required=True)
    comentario = fields.Text(string='Comentario', size=10)
    fecha_factura= fields.Date(string='Fecha de factura', size=50, required=True)


    administrador_id=fields.Many2one(comodel_name='neuroeduka.administrador', string='Administrador', required=True)
    periodo_id=fields.Many2one(comodel_name='neuroeduka.periodo', string='Periodo', required=True)
    detalle_factura_ids = fields.One2many(
        comodel_name='neuroeduka.detalle_factura', inverse_name='factura_id',string='Detalle de Factura', required=True)
    resultado_operacional_ids = fields.One2many(
        comodel_name='neuroeduka.resultado_operacional', inverse_name='factura_id',string='Resultado Operacional', required=True)

class Periodo(models.Model):
    _name = 'neuroeduka.periodo'
    _rec_name = 'nombre_periodo'

    nombre_periodo = fields.Char(string='Nombre Periodo', size=50, required=True)
   
    boleta_pago_ids = fields.One2many(
       comodel_name='neuroeduka.boleta_pago', inverse_name='periodo_id',string='Boletas', required=True)
    factura_ids = fields.One2many(
        comodel_name='neuroeduka.factura', inverse_name='periodo_id',string='Factura', required=True)  
    resultado_operacional_ids = fields.One2many(
        comodel_name='neuroeduka.resultado_operacional', inverse_name='periodo_id',string='Resultado Operacional', required=True)

class Resultado_Operacional(models.Model):
    _name = 'neuroeduka.resultado_operacional'
    _rec_name = 'result_final'

    result_final = fields.Integer(string='Resultado Final', size=50, required=True)
    fecha_resultado = fields.Date(string='Fecha Resultado', size=10, required=True)
    periodo_id = fields.Many2one(comodel_name='neuroeduka.periodo', string='Periodo', required=True)
    factura_id=fields.Many2one(comodel_name='neuroeduka.factura', string='Factura', required=True)
    boleta_pago_id=fields.Many2one(comodel_name='neuroeduka.boleta_pago', string='Boleta de Pago', required=True)

class Boleta_Pago(models.Model):
    _name = 'neuroeduka.boleta_pago'
    _rec_name = 'monto_pagar'

    monto_pagar = fields.Integer(string='Monto a Pagar', size=50, required=True)
    fecha_pago = fields.Date(string='Fecha de Pago', size=10, required=True)
    prevision = fields.Selection([('fonasa', 'Fonasa'), ('isapre', 'Isapre'), (
        'particular', 'Particular')], string='Previsión', required=True)
    medio_pago = fields.Selection([('transferencia', 'Transferencia'), ('efectivo', 'Efectivo'), (
        'Débito', 'Débito'), ('credito', 'Crédito')], string='Medio de Pago', required=True)
    num_voucher= fields.Integer(string='Numero de Comprobante', size=50, required=True)
    motivo_consulta_id=fields.Many2many(comodel_name='neuroeduka.motivo_consulta', string='Motivo(s) de Pago', required=True)
    paciente_id=fields.Many2one(comodel_name='neuroeduka.paciente', string='Paciente', required=True)
    especialista_id=fields.Many2one(comodel_name='neuroeduka.especialista', string='Especialista', required=True)
    periodo_id=fields.Many2one(comodel_name='neuroeduka.periodo', string='Periodo', required=True)
    
    resultado_operacional_ids = fields.One2many(
        comodel_name='neuroeduka.resultado_operacional', inverse_name='boleta_pago_id',string='Resultado Operacional', required=True)

class Evolucion(models.Model):
    _name = 'neuroeduka.evolucion'
    _rec_name = 'fecha_evolucion'

    paciente_id=fields.Many2one(comodel_name='neuroeduka.paciente', string='Paciente', required=True)
    especialista_id=fields.Many2one(comodel_name='neuroeduka.especialista', string='Especialista', required=True)
    fecha_evolucion= fields.Date(string='Fecha', required=True)
    quien_consulta = fields.Char(string="Quién Consulta", required=True)
    antecedente_familiar= fields.Text(string="Antecedentes Familiares")
    antecedente_escolar= fields.Text(string="Antecedentes Escolares o Laborales")
    proceso= fields.Text(string="Proceso")
    objetivo= fields.Text(string="Objetivos")
    recurso_id=fields.Many2many(comodel_name='neuroeduka.recurso', string='Recursos Terapeuticos', required=True)
    sugerencia = fields.Text(string="Sugerencias")
    prox_sesion= fields.Char(string="Próxima Sesión")

class Recurso(models.Model):
    _name = 'neuroeduka.recurso'
    _rec_name = 'nombre_recurso'

    nombre_recurso= fields.Char(string='Nombre Recurso Terapeutico', required=True)
    evolucion_ids= fields.One2many(comodel_name='neuroeduka.evolucion', inverse_name='recurso_id',string='Evolucion', required=True)

class Dato_Anamnesico(models.Model):
    _name = 'neuroeduka.dato_anamnesico'
    _rec_name = 'motivo_consultad'

    paciente_id=fields.Many2one(comodel_name='neuroeduka.paciente', string='Paciente', required=True)
    fecha=fields.Date(string='Fecha', required=True)
    motivo_consultad = fields.Text(string='Motivo de la Consulta', required=True)
    antecedente_clinico = fields.Text(string='Antecedentes Clínicos', required=True)
    descripcion_mama = fields.Text(string='Descripción Mamá' )
    descripcion_papa = fields.Text(string='Descripción Papá' )
    area_escolar = fields.Text(string='Área Escolar',  required=True)
    area_academica = fields.Text(string='Área Académica',  required=True)
    area_afectiva = fields.Text(string='Área Afectiva',  required=True)
    area_social = fields.Text(string='Área Social', required=True)
    
    embarazo = fields.Selection([('programado', 'Programado'), ('controlado', 'Controlado')], string='Embarazo', required=True)
    consumo_embarazo = fields.Char(string='Consumo durante el embarazo (OH, Drogas, Tabaco, Medicamentos)', size=50, required=True)
    enfermedad_embarazo= fields.Char(string='Enfermedades durante el embarazo', size=50, required=True)
    parto = fields.Selection([('normal', 'Normal'), ('cesaria', 'Cesaria')], string='Parto', required=True)
    forse = fields.Char(string='Forse', size=50, required=True)
    peso = fields.Integer(string='Peso', size=50, required=True)
    talla = fields.Char(string='Talla', size=50, required=True)    
    semanas_gestacion = fields.Integer(string='Semanas de gestación', size=50, required=True)

   
    enfermedad = fields.Char(string='Enfermedades', size=50, required=True)
    sueno= fields.Char(string='Sueño', size=50, required=True)
    alimentacion = fields.Char(string='Alimentación', size=50, required=True)
    apego = fields.Char(string='Apego', size=50, required=True)
    observacion = fields.Text(string='Observaciones', required=True)    

    balbuceo = fields.Char(string='Balbuceo', size=50, required=True)
    primera_palabra= fields.Char(string='Primeras palabras', size=50, required=True)
    frase_dospalabras = fields.Char(string='Frase de dos palabras', size=50, required=True)
    frase_compleja = fields.Char(string='Frases Complejas', size=50, required=True)
    observacion_l = fields.Text(string='Observaciones', size=50, required=True)    


    tepsi = fields.Char(string='TEPSI', size=50, required=True)
    control_encefalico = fields.Char(string='Control Encefálico', size=50, required=True)
    sedestacion = fields.Char(string='Sedestación', size=50, required=True)
    gateo = fields.Char(string='Gateo ', size=50, required=True)
    perdida_h = fields.Char(string='Pérdida H. Sostener', size=50, required=True)
    h_motor = fields.Char(string='H. Motoras (Postura, Marcha o Coord.)', size=50, required=True)       
    h_avd = fields.Char(string='H. AVD (Comer, Asearse, Vestirse)', size=50, required=True)
    juego_imag= fields.Char(string='Juegos Imag. o Constru.', size=50, required=True)
    interaccion = fields.Char(string='Interración o Respuesta Social ', size=50, required=True)
    observacion_d = fields.Text(string='Observaciones',required=True)   

    diurno = fields.Char(string='Diurno', size=50, required=True)
    nocturno = fields.Char(string='Nocturno', size=50, required=True)
    vesical = fields.Char(string='Vesical', size=50, required=True)
    intestinal = fields.Char(string='Intestinal', size=50, required=True)
    observacion_e = fields.Text(string='Observaciones', required=True)   

    sueno = fields.Selection([('normal', 'Normal'), ('intranquilo', 'Intranquilo')], string='Sueño', required=True)
    dificultad_inicio = fields.Char(string='Dificultades Inicio', size=50, required=True)
    insonmio = fields.Char(string='Insomnio', size=50, required=True)
    hora_despierta = fields.Char(string='Hora Despierta', size=50, required=True)
    hora_acostarse = fields.Char(string='Hora de Acostarse', size=50, required=True)   
    observacion_s = fields.Text(string='Observaciones', required=True)

    
    area_familiar = fields.Text(string='Área Familiar', required=True)
    area_personal = fields.Text(string='Área Personal', required=True)
    juego = fields.Text(string='Juegos (Funcionales y/o Simbólicos)', required=True)
    rutina_actual = fields.Text(string='Rutina Actual', required=True)
    ant_morbidos_familiar = fields.Text(string='Antecedentes Mórbidos Familiares',  required=True)
    ant_morbidos_personal = fields.Text(string='Antecedentes Mórbidos Personales', required=True)
    hipotesis = fields.Text(string='Hipótesis y Sugerencias', required=True)
    actitud = fields.Text(string='Actitud durante la entrevista', required=True)
   
    centro_educativo_ids = fields.One2many(
        comodel_name='neuroeduka.centro_educativo', inverse_name='dato_anamnesico_id',string='Centros Educativos', required=True)
    
class Centro_Educativo(models.Model):
    _name = 'neuroeduka.centro_educativo'
    _rec_name = 'nombre_centro'

    dato_anamnesico_id=fields.Many2one(comodel_name='neuroeduka.dato_anamnesico', string='Folio', required=True)
    
    nombre_centro = fields.Char(string='Nombre Centro Educativo', size=50, required=True)
    tipo_centro = fields.Char(string='Tipo de Centro', size=10, required=True)
    nivel_centro = fields.Char(string='Nivel', size=10, required=True)
    fecha_asistencia = fields.Char(string='Fecha de Asistencia', size=10, required=True)
    ayuda_adicional = fields.Char(string='Ayuda Adicional Requerida', size=10, required=True)

  