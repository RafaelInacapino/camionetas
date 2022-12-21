from django.urls import path, include, re_path
from . import views
 
urlpatterns = [

    #Home Start
    path('', views.home_user),

    path('crud_agenda_inicial1/', views.crud_agenda_inicial1, name='crud_agenda_inicial1'),
    path('crud_agenda_inicial1_editar/<pk>/', views.crud_agenda_inicial1_editar, name='crud_agenda_inicial1_editar'),
    path('crud_agenda_inicial1_listar/', views.crud_agenda_inicial1_listar, name='crud_agenda_inicial1_listar'), 
    path('reserva_inicial1_Add/',views.reserva_inicial1_Add, name='reserva_inicial1_Add'),
    path('reserva_inicial1_Del/<pk>/',views.reserva_inicial1_Del, name='reserva_inicial1_Del'),
    path('reserva_inicial1_Edit/<pk>/',views.reserva_inicial1_Edit, name='reserva_inicial1_Edit'),
    
    path('crud_agenda_inicial2/', views.crud_agenda_inicial2, name='crud_agenda_inicial2'),
    path('crud_agenda_inicial2_editar/<pk>/', views.crud_agenda_inicial2_editar, name='crud_agenda_inicial2_editar'),
    path('crud_agenda_inicial2_listar/', views.crud_agenda_inicial2_listar, name='crud_agenda_inicial2_listar'), 
    path('reserva_inicial2_Add/',views.reserva_inicial2_Add, name='reserva_inicial2_Add'),
    path('reserva_inicial2_Del/<pk>/',views.reserva_inicial2_Del, name='reserva_inicial2_Del'),
    path('reserva_inicial2_Edit/<pk>/',views.reserva_inicial2_Edit, name='reserva_inicial2_Edit'),
    
    path('crud_agenda_final1/',views.crud_agenda_final1,name='crud_agenda_final1'),
    path('crud_agenda_final1_editar/<pk>/', views.crud_agenda_final1_editar, name='crud_agenda_final1_editar'),
    path('crud_agenda_final1_listar/', views.crud_agenda_final1_listar, name='crud_agenda_final1_listar'), 
    path('reserva_final1_Add/',views.reserva_final1_Add, name='reserva_final1_Add'),
    path('reserva_final1_Del/<pk>/',views.reserva_final1_Del, name='reserva_final1_Del'),
    path('reserva_final1_Edit/<pk>/',views.reserva_final1_Edit, name='reserva_final1_Edit'),
    
    path('crud_agenda_final2/',views.crud_agenda_final2,name='crud_agenda_final2'),
    path('crud_agenda_final2_editar/<pk>/', views.crud_agenda_final2_editar, name='crud_agenda_final2_editar'),
    path('crud_agenda_final2_listar/', views.crud_agenda_final2_listar, name='crud_agenda_final2_listar'), 
    path('reserva_final2_Add/',views.reserva_final2_Add, name='reserva_final2_Add'),
    path('reserva_final2_Del/<pk>/',views.reserva_final2_Del, name='reserva_final2_Del'),
    path('reserva_final2_Edit/<pk>/',views.reserva_final2_Edit, name='reserva_final2_Edit'),
    
    path('crud_usuarios/', views.crud_usuarios, name='crud_usuarios'),
    
    path('crud_vehiculos/', views.crud_vehiculos, name='crud_vehiculos'),
    path('crud_vehiculos_editar/', views.crud_vehiculos_editar, name='crud_vehiculos_editar'),
    path('crud_vehiculos_listar/', views.crud_vehiculos_listar, name='crud_vehiculos_listar'),
    path('vehiculos_add/', views.vehiculos_add, name='vehiculos_add'),
    path('vehiculos_del/<pk>/', views.vehiculos_del, name='vehiculos_del'),
    path('vehiculos_edit/<pk>/', views.vehiculos_edit, name='vehiculos_edit'),
    

    path('home_user/', views.home_user, name='home_user'),
    path('home_admin/', views.home_admin, name='home_admin'),
    path('mi_perfil/', views.mi_perfil, name='mi_perfil'),
    path('mi_perfil_editar_datos/', views.mi_perfil_editar_datos, name='mi_perfil_editar_datos'),
    path('mi_perfil_historial_solicitudes/', views.mi_perfil_historial_solicitudes, name='mi_perfil_historial_solicitudes'),
    path('listado_conductores/', views.listado_conductores, name='listado_conductores'),
    path('listado_reservas1/', views.listado_reservas1, name='listado_reservas1'),
    path('listado_reservas1_solicitudes_anteriores/', views.listado_reservas1_solicitudes_anteriores, name='listado_reservas1_solicitudes_anteriores'),
    path('listado_reservas2/', views.listado_reservas2, name='listado_reservas2'),
    path('listado_reservas2_solicitudes_anteriores/', views.listado_reservas2_solicitudes_anteriores, name='listado_reservas2_solicitudes_anteriores'),
    path('formulario_agenda_inicial1/', views.formulario_agenda_inicial1, name='formulario_agenda_inicial1'),
    path('formulario_agenda_inicial2/', views.formulario_agenda_inicial2, name='formulario_agenda_inicial2'),
    path('formulario_agenda_final1/', views.formulario_agenda_final1, name='formulario_agenda_final1'),
    path('formulario_agenda_final2/', views.formulario_agenda_final2, name='formulario_agenda_final2'),
    path('opcion_reserva',views.opcion_reserva, name='opcion_reserva'),
    path('opcion_retorno',views.opcion_retorno, name='opcion_retorno'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    #path('register/', views.register, name='register'),
    
    
    path('reserva_inicial1/', views.reserva_inicial1, name='reserva_inicial1'),
    path('reserva_inicialuser1_Add/',views.reserva_inicialuser1_Add, name='reserva_inicialuser1_Add'),
    path('reserva_inicial2/', views.reserva_inicial2, name='reserva_inicial2'),
    path('reserva_inicialuser2_Add/',views.reserva_inicialuser2_Add, name='reserva_inicialuser2_Add'),
    path('reserva_final1/', views.reserva_final1, name='reserva_final1'),
    path('reserva_finaluser1_Add/',views.reserva_finaluser1_Add, name='reserva_finaluser1_Add'),
    path('reserva_final2/', views.reserva_final2, name='reserva_final2'),
    path('reserva_finaluser2_Add/',views.reserva_finaluser2_Add, name='reserva_finaluser2_Add'),
    
    # users system
    path('cuenta/', include('django.contrib.auth.urls')),
    path('cuenta/register',views.registro),
    path('cuenta/successlogin',views.successlogin),
]   
