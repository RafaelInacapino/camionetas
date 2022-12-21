from django.shortcuts import render
from django.shortcuts import redirect
from .models import Usuario, Vehiculo,Reserva_Inicial1,Reserva_Inicial2
from reservas.forms import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from reservas.decorators import login_required, superuser_required



# Create your views here.

# views users log system
def successlogin(request):
    context = {}
    return render(request,'registration/success.html',context)

def registro(request):
    # context dict
    context = {}

    #Script
    if request.method == 'POST':
        print('Method is "POST"')
        form = RegisterUserForm(request.POST)
        # RegisterUserForm is created from User model, all model field restrictions are checked to considerate it a valid form
        if form.is_valid():
            print('Form is "VALID"')
            # Save user to database but with is_active = False
            user = form.save(commit=False)
            user.is_active = True
            user.is_superuser = False
            user.is_staff = False
            user.save()
            context["mensaje"] = "Registrado con Éxito."
            return redirect('/reservas/cuenta/register')
        else:
            print('Form is "NOT VALID"')
            context['form'] = RegisterUserForm(request.POST)
            context["mensaje"] = "Error al Registrar."
            return render(request, 'registration/registrar.html', context)
    else:
        print('Method is "NOT POST"')
        form = RegisterUserForm()
        context['form'] = form
        return render(request, 'registration/registrar.html', context)

def login_error(request):
    return render(request, 'login_error.html')

@superuser_required
def home_admin(request):
    return render(request, 'home_admin.html')

@superuser_required
def crud_agenda_inicial1(request):
    context={}
    return render(request, 'crud_agenda_inicial1.html',context)

@superuser_required
def crud_agenda_inicial2(request):
    return render(request, 'crud_agenda_inicial2.html')

@superuser_required
def crud_agenda_inicial1_editar(request):
    return render(request, 'crud_agenda_inicial1_editar.html')

@superuser_required
def crud_agenda_inicial1_listar(request):
    reservas_iniciales1=Reserva_Inicial1.objects.all()
    return render (request, 'crud_agenda_inicial1_listar.html',{"reserva_inicial1":reservas_iniciales1})

@superuser_required
def crud_agenda_inicial2_editar(request):
    return render(request, 'crud_agenda_inicial2_editar.html')

@superuser_required
def crud_agenda_inicial2_listar(request):
    reservas_iniciales2=Reserva_Inicial2.objects.all()
    return render (request, 'crud_agenda_inicial2_listar.html',{"reserva_inicial2":reservas_iniciales2})

@superuser_required
def crud_agenda_final1(request):
    return render(request, 'crud_agenda_final1.html')

@superuser_required
def crud_agenda_final1_editar(request):
    return render(request, 'crud_agenda_final1_editar.html')

@superuser_required
def crud_agenda_final1_listar(request):
    reservas_finales1=Reserva_Final1.objects.all()
    return render (request, 'crud_agenda_final1_listar.html',{"reserva_final1":reservas_finales1})

@superuser_required
def crud_agenda_final2(request):
    return render(request, 'crud_agenda_final2.html')

@superuser_required
def crud_agenda_final2_editar(request):
    return render(request, 'crud_agenda_final2_editar.html')

@superuser_required
def crud_agenda_final2_listar(request):
    reservas_finales2=Reserva_Final2.objects.all()
    return render (request, 'crud_agenda_final2_listar.html',{"reserva_final2":reservas_finales2})

@superuser_required
def crud_usuarios(request):
    return render(request, 'crud_usuarios.html')

@superuser_required
def crud_vehiculos(request):
    return render(request, 'crud_vehiculos.html')

@superuser_required
def crud_vehiculos_editar(request):
    return render(request, 'crud_vehiculos_editar.html')

@superuser_required
def vehiculos_add(request):
    print ("estoy en controlador vehiculos_add... ")
    context = {}
    if request.method == "POST":
        print ("controlador es un POST... ")
        opcion = request.POST.get("opcion","")
        
        print(request.FILES)
       
    
        if True:
            
            id_vehiculo = request.POST.get("id_vehiculo")
            patente = request.POST["patente"]
            marca = request.POST["marca"] 
            modelo = request.POST["modelo"]
            anio = request.POST["anio"]
           
            
            
            if id_vehiculo != "":
                
                vehiculo = Vehiculo()
                
                vehiculo.id_vehiculo = id_vehiculo
                vehiculo.patente = patente
                vehiculo.marca = marca
                vehiculo.modelo = modelo
                vehiculo.anio = anio
                
                
                vehiculo.save()
                
                context={"mensaje":"Vehiculo agregado correctamente"}
            else:
                context={"mensaje": "Error, los campos no pueden estar vacios"}
              
        
    return render (request, 'crud_vehiculos.html', context)

@superuser_required
def vehiculos_del (request, pk):  
    vehiculo = Vehiculo.objects.get(id_vehiculo=pk)
    context={}
    if vehiculo:
        vehiculo.delete()
        return redirect(to='crud_vehiculos_listar')
   
@superuser_required 
def vehiculos_edit (request, pk):

    vehiculo = Vehiculo.objects.get(id_vehiculo=pk)

    datos = {
        'form': VehiculoForm(instance=vehiculo)
    }

    if request.method == 'POST':
        formulario2 = VehiculoForm(data=request.POST, instance=vehiculo)
        if formulario2.is_valid:
            formulario2.save(),
            datos['mensaje'] = "Los cambios han sido modificados correctamente"  
    return render(request, 'crud_vehiculos_editar.html', datos)

@superuser_required
def crud_vehiculos_listar(request):
    vehiculos=Vehiculo.objects.all()
    data = {'vehiculo':vehiculos}
    return render (request, 'crud_vehiculos_listar.html',data)

def home_user(request):
    return render(request, 'home_user.html')

def mi_perfil(request):
    return render(request, 'mi_perfil.html')

def mi_perfil_editar_datos(request):
    return render(request, 'mi_perfil_editar_datos.html')

def mi_perfil_historial_solicitudes(request):
    return render(request, 'mi_perfil_historial_solicitudes.html')

def listado_conductores(request):
    return render(request, 'listado_conductores.html')

def listado_reservas1(request):
    return render(request, 'listado_reservas1.html')

def listado_reservas1_solicitudes_anteriores(request):
    return render(request, 'listado_reservas1_solicitudes_anteriores.html')

def listado_reservas2(request):
    return render(request, 'listado_reservas2.html')

def listado_reservas2_solicitudes_anteriores(request):
    return render(request, 'listado_reservas2_solicitudes_anteriores.html')

def formulario_agenda_inicial1(request):
    return render(request, 'formulario_agenda_inicial1.html')

def formulario_agenda_inicial2(request):
    return render(request, 'formulario_agenda_inicial2.html')

def formulario_agenda_final1(request):
    return render(request, 'formulario_agenda_final1.html')

def formulario_agenda_final2(request):
    return render(request, 'formulario_agenda_final2.html')

def cerrar_sesion(request):
    return render(request, 'cerrar_sesion.html')

def usuariosAdd(request):
    print ("estoy en controlador usuariosAdd... ")
    context = {}
    if request.method == "POST":
        print ("controlador es un POST... ")
        opcion = request.POST.get("opcion","")

        if opcion=="Agregar":
            
            rut = request.POST["rut"]
            nombre = request.POST["nombre"]
            apellido_paterno = request.POST["apellido_paterno"]
            apellido_materno = request.POST["apellido_materno"]
            fecha_nacimiento = request.POST["fecha_nacimiento"]
            genero = request.POST["genero"]
            
            
            if rut != "" and nombre != "":
                
                usuario = Usuario()
                
                usuario.rut = rut
                usuario.nombre = nombre
                usuario.apellido_paterno = apellido_paterno
                usuario.apellido_materno = apellido_materno
                usuario.fecha_nacimiento = fecha_nacimiento
                usuario.genero = genero
                
                usuario.save()
                context["mensaje"] = "Guardado correctamente"
            else:
                context["mensaje"] = "Error"
        
    return render (request, 'tdguitarras/adminusuarios.html', context)

def reserva_inicial1_Add(request):
    print ("estoy en controlador reserva_inicial1Add... ")
    context = {}
    if request.method == "POST":
        print ("controlador es un POST... ")
        opcion = request.POST.get("opcion","")
        
        print(request.FILES)
       
    
        if True:
            
            motivo1 = request.POST["motivo1"]
            direccion1 = request.POST["direccion1"]
            foto_tacometro1 = request.FILES.get("foto_tacometro1")
            
            if id != "" and motivo1 != "": 
                
                reserva_inicial1 = Reserva_Inicial1()
                
                
                
                reserva_inicial1.motivo1 = motivo1
                reserva_inicial1.direccion1 = direccion1
                reserva_inicial1.foto_tacometro1 = foto_tacometro1
                
                reserva_inicial1.save()
                
                context={"mensaje":"reserva inicial 1 agregado correctamente"}
            else:
                context={"mensaje": "Error, los campos no pueden estar vacios"}
        else:
            context={"mensaje": "Error, los campos no pueden estar vacios"}
            return render (request, 'home_admin.html', context)         
        
    return render (request, 'crud_agenda_inicial1.html', context)

def reserva_inicial1_Del(request,pk):
    reserva_inicial1 = Reserva_Inicial1.objects.get(id=pk)
    context={}
    if reserva_inicial1:
        reserva_inicial1.delete()
        return redirect(to='crud_agenda_inicial1_listar')
    
def reserva_inicial1_Edit (request, pk):

    reserva_inicial1 = Reserva_Inicial1.objects.get(id=pk)

    datos = {
        'form': Reserva_Inicial1Form(instance=reserva_inicial1)
    }

    if request.method == 'POST':
        formulario1 = Reserva_Inicial1Form(data=request.POST, instance=reserva_inicial1)
        if formulario1.is_valid:
            formulario1.save(),
            datos['mensaje'] = "Los cambios han sido modificados correctamente"  
    return render(request, 'crud_agenda_inicial1_editar.html', datos)      

def reserva_inicial2_Add(request):
    print ("estoy en controlador reserva_inicial1Add... ")
    context = {}
    if request.method == "POST":
        print ("controlador es un POST... ")
        opcion = request.POST.get("opcion","")
        
        print(request.FILES)
       
    
        if True:
            
            motivo2 = request.POST["motivo2"]
            direccion2 = request.POST["direccion2"]
            foto_tacometro2 = request.FILES.get("foto_tacometro2")
            
            if id != "" and motivo2 != "": 
                
                reserva_inicial2 = Reserva_Inicial2()
                
                
                
                reserva_inicial2.motivo2 = motivo2
                reserva_inicial2.direccion2 = direccion2
                reserva_inicial2.foto_tacometro2 = foto_tacometro2
                
                reserva_inicial2.save()
                
                context={"mensaje":"reserva inicial 2 agregado correctamente"}
            else:
                context={"mensaje": "Error, los campos no pueden estar vacios"}
        else:
            context={"mensaje": "Error, los campos no pueden estar vacios"}
            return render (request, 'home_admin.html', context)         
        
    return render (request, 'crud_agenda_inicial2.html', context)

def reserva_inicial2_Del(request,pk):
    reserva_inicial2 = Reserva_Inicial2.objects.get(id=pk)
    context={}
    if reserva_inicial2:
        reserva_inicial2.delete()
        return redirect(to='crud_agenda_inicial2_listar')
    
def reserva_inicial2_Edit (request, pk):

    reserva_inicial2 = Reserva_Inicial2.objects.get(id=pk)

    datos = {
        'form': Reserva_Inicial2Form(instance=reserva_inicial2)
    }

    if request.method == 'POST':
        formulario2 = Reserva_Inicial2Form(data=request.POST, instance=reserva_inicial2)
        if formulario2.is_valid:
            formulario2.save(),
            datos['mensaje'] = "Los cambios han sido modificados correctamente"  
    return render(request, 'crud_agenda_inicial2_editar.html', datos)      

def reserva_final1_Add(request):
    print ("estoy en controlador reserva_final1Add... ")
    context = {}
    if request.method == "POST":
        print ("controlador es un POST... ")
        opcion = request.POST.get("opcion","")
        
        print(request.FILES)
       
    
        if True:
            
            observaciones1 = request.POST["observaciones1"]
            foto_tacometro_final1 = request.FILES.get("foto_tacometro_final1")
            recarga_combustible1 = request.FILES.get("recarga_combustible1")
            
            if id != "" and observaciones1 != "": 
                
                reserva_final1 = Reserva_Final1()
                
                
                
                reserva_final1.observaciones1 = observaciones1
                reserva_final1.foto_tacometro_final1 = foto_tacometro_final1
                reserva_final1.recarga_combustible1 = recarga_combustible1
                
                reserva_final1.save()
                
                context={"mensaje":"reserva final 1 agregado correctamente"}
            else:
                context={"mensaje": "Error, los campos no pueden estar vacios"}
        else:
            context={"mensaje": "Error, los campos no pueden estar vacios"}
            return render (request, 'home_admin.html', context)         
        
    return render (request,'crud_agenda_final2.html', context)

def reserva_final1_Del(request,pk):
    reserva_final1 = Reserva_Final1.objects.get(id=pk)
    context={}
    if reserva_final1:
        reserva_final1.delete()
        return redirect(to='crud_agenda_final1_listar')
    
def reserva_final1_Edit (request, pk):

    reserva_final1 = Reserva_Final1.objects.get(id=pk)

    datos = {
        'form': Reserva_Final1Form(instance=reserva_final1)
    }

    if request.method == 'POST':
        formulario1 = Reserva_Final1Form(data=request.POST, instance=reserva_final1)
        if formulario1.is_valid:
            formulario1.save(),
            datos['mensaje'] = "Los cambios han sido modificados correctamente"  
    return render(request, 'crud_agenda_final1_editar.html', datos)   
    
def reserva_final2_Add(request):
    print ("estoy en controlador reserva_final2Add... ")
    context = {}
    if request.method == "POST":
        print ("controlador es un POST... ")
        opcion = request.POST.get("opcion","")
        
        print(request.FILES)
       
    
        if True:
            
            observaciones2 = request.POST["observaciones2"]
            foto_tacometro_final2 = request.FILES.get("foto_tacometro_final2")
            recarga_combustible2 = request.FILES.get("recarga_combustible2")
            
            if id != "" and observaciones2 != "": 
                
                reserva_final2 = Reserva_Final2()
                
                
                
                reserva_final2.observaciones2 = observaciones2
                reserva_final2.foto_tacometro_final2 = foto_tacometro_final2
                reserva_final2.recarga_combustible2 = recarga_combustible2
                
                reserva_final2.save()
                
                context={"mensaje":"reserva final 2 agregado correctamente"}
            else:
                context={"mensaje": "Error, los campos no pueden estar vacios"}
        else:
            context={"mensaje": "Error, los campos no pueden estar vacios"}
            return render (request, 'home_admin.html', context)         
        
    return render (request, 'crud_agenda_final2.html', context)

def reserva_final2_Del(request,pk):
    reserva_final2 = Reserva_Final2.objects.get(id=pk)
    context={}
    if reserva_final2:
        reserva_final2.delete()
        return redirect(to='crud_agenda_final2_listar')
    
def reserva_final2_Edit (request, pk):

    reserva_final2 = Reserva_Final2.objects.get(id=pk)

    datos = {
        'form': Reserva_Final2Form(instance=reserva_final2)
    }

    if request.method == 'POST':
        formulario1 = Reserva_Final2Form(data=request.POST, instance=reserva_final2)
        if formulario1.is_valid:
            formulario1.save(),
            datos['mensaje'] = "Los cambios han sido modificados correctamente"  
    return render(request, 'crud_agenda_final2_editar.html', datos)   
    
@login_required
def opcion_reserva(request):
    return render(request,'opcion_reserva.html')

def reserva_inicial1(request):
    context={}
    return render(request, 'reserva_inicial1.html',context)

def reserva_inicial2(request):
    context={}
    return render(request, 'reserva_inicial2.html',context)

@login_required
def opcion_retorno(request):
    return render(request,'opcion_retorno.html')

def reserva_final1(request):
    context={}
    return render(request, 'reserva_final1.html',context)

def reserva_final2(request):
    context={}
    return render(request, 'reserva_final2.html',context)


def reserva_inicialuser1_Add(request):
    print ("estoy en controlador reserva_inicial1Add... ")
    context = {}
    if request.method == "POST":
        print ("controlador es un POST... ")
        opcion = request.POST.get("opcion","")
        
        print(request.FILES)
       
    
        if True:
            
            motivo1 = request.POST["motivo1"]
            direccion1 = request.POST["direccion1"]
            foto_tacometro1 = request.FILES.get("foto_tacometro1")
            
            if id != "" and motivo1 != "": 
                
                reserva_inicial1 = Reserva_Inicial1()
                
                
                
                reserva_inicial1.motivo1 = motivo1
                reserva_inicial1.direccion1 = direccion1
                reserva_inicial1.foto_tacometro1 = foto_tacometro1
                
                reserva_inicial1.save()
                
                context={"mensaje":"reserva inicial 1 agregado correctamente"}
            else:
                context={"mensaje": "Error, los campos no pueden estar vacios"}
        else:
            context={"mensaje": "Error, los campos no pueden estar vacios"}
            return render (request, 'home_admin.html', context)         
        
    return render (request, 'reserva_inicial1.html', context)


def reserva_inicialuser2_Add(request):
    print ("estoy en controlador reserva_inicialuser2Add... ")
    context = {}
    if request.method == "POST":
        print ("controlador es un POST... ")
        opcion = request.POST.get("opcion","")
        
        print(request.FILES)
       
    
        if True:
            
            motivo2 = request.POST["motivo2"]
            direccion2 = request.POST["direccion2"]
            foto_tacometro2 = request.FILES.get("foto_tacometro2")
            
            if id != "" and motivo2 != "": 
                
                reserva_inicial2 = Reserva_Inicial2()
                
                
                
                reserva_inicial2.motivo2 = motivo2
                reserva_inicial2.direccion2 = direccion2
                reserva_inicial2.foto_tacometro2 = foto_tacometro2
                
                reserva_inicial2.save()
                
                context={"mensaje":"reserva inicial 2 agregado correctamente"}
            else:
                context={"mensaje": "Error, los campos no pueden estar vacios"}
        else:
            context={"mensaje": "Error, los campos no pueden estar vacios"}
            return render (request, 'home_admin.html', context)         
        
    return render (request, 'reserva_inicial2.html', context)


def reserva_finaluser1_Add(request):
    print ("estoy en controlador reserva_finaluser1Add... ")
    context = {}
    if request.method == "POST":
        print ("controlador es un POST... ")
        opcion = request.POST.get("opcion","")
        
        print(request.FILES)
       
    
        if True:
            
            observaciones1 = request.POST["observaciones1"]
            foto_tacometro_final1 = request.FILES.get("foto_tacometro_final1")
            recarga_combustible1 = request.FILES.get("recarga_combustible1")
            
            if id != "" and observaciones1 != "": 
                
                reserva_final1 = Reserva_Final1()
                
                
                
                reserva_final1.observaciones1 = observaciones1
                reserva_final1.foto_tacometro_final1 = foto_tacometro_final1
                reserva_final1.recarga_combustible1 = recarga_combustible1
                
                reserva_final1.save()
                
                context={"mensaje":"reserva final 1 agregado correctamente"}
            else:
                context={"mensaje": "Error, los campos no pueden estar vacios"}
        else:
            context={"mensaje": "Error, los campos no pueden estar vacios"}
            return render (request, 'home_admin.html', context)         
        
    return render (request,'reserva_final1.html', context)


def reserva_finaluser2_Add(request):
    print ("estoy en controlador reserva_finaluser2Add... ")
    context = {}
    if request.method == "POST":
        print ("controlador es un POST... ")
        opcion = request.POST.get("opcion","")
        
        print(request.FILES)
       
    
        if True:
            
            observaciones2 = request.POST["observaciones2"]
            foto_tacometro_final2 = request.FILES.get("foto_tacometro_final2")
            recarga_combustible2 = request.FILES.get("recarga_combustible2")
            
            if id != "" and observaciones2 != "": 
                
                reserva_final2 = Reserva_Final2()
                
                
                
                reserva_final2.observaciones2 = observaciones2
                reserva_final2.foto_tacometro_final2 = foto_tacometro_final2
                reserva_final2.recarga_combustible2 = recarga_combustible2
                
                reserva_final2.save()
                
                context={"mensaje":"reserva final 2 agregado correctamente"}
            else:
                context={"mensaje": "Error, los campos no pueden estar vacios"}
        else:
            context={"mensaje": "Error, los campos no pueden estar vacios"}
            return render (request, 'home_admin.html', context)         
        
    return render (request, 'reserva_final2.html', context)