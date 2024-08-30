class Paciente:
    def __init__(self) -> None:
        self.__nombre= ''
        self.__cedula= 0
        self.__genero= ''
        self.__servicio= ''
    
    def VerNombre(self):
        return self.__nombre
    def VerCedula(self):
        return self.__cedula
    def VerGenero(self):
        return self.__genero
    def VerServicio(self):
        return self.__servicio
    
    def AsignarNombre(self,n):
        self.__nombre= n
    def AsignarCedula(self,c):
        self.__cedula= c
    def AsignarGenero(self,g):
        self.__genero= g
    def AsignarServicio(self,s):
        self.__servicio= s
        

class Sistema: 
    def __init__(self) -> None:
        self.__ListaPacientes = []
        
    def IngresarPaciente(self,pac):
        self.__ListaPacientes.append(pac)
        
    def VerDatos(self,c): 
        for p in self.__ListaPacientes:
            if c==p.VerCedula():
                return p 
    
    def VerNumeroPacientes(self): 
        print(f'En el sistema hay {str(len(self.__ListaPacientes))} pacientes almacenados')
        

def main():
    s=Sistema()
    while True: 
        op=int(input('''Ingrese una opcion:
                     1. Ingresar paciente
                     2. Ver paciente
                     3. Ver numero de pacientes
                     4. Salir
                     '''))
        if op==1:
            print('Ingrese los datos del paciente que se le solicitaran a continuacion')
            nombre=input('Nombre: ')
            cedula=int(input('Cedula: '))
            genero=input('Genero: ')
            servicio=input('Servicio: ')
            
            p=Paciente()
            p.AsignarNombre(nombre)
            p.AsignarCedula(cedula)
            p.AsignarGenero(genero)
            p.AsignarServicio(servicio)
            s.IngresarPaciente(p)

        elif op==2: 
            c=int(input('Ingrese la cedula del paciente que desea buscar: '))
            pac=s.VerDatos(c)
            
            print(f'Nombre: {pac.VerNombre()}')
            print(f'Cedula: {pac.VerCedula()}')
            print(f'Genero: {pac.VerGenero()}')
            print(f'Servicio: {pac.VerServicio()}')
        
        elif op==3:
            s.VerNumeroPacientes()
        
        elif op==4:
            break
        
        else: 
            print('Opcion no valida')
            
if __name__=='__main__':
    main()
            
            
            
        
        
        
        







# class Sistema:
#     def __init__(self) -> None:
#         self.__ListaPacientes= []
#         self.__NumeroPacientes= len(self.__ListaPacientes)
    
    
#     def IngresarPaciente(self):
#         nombre=input('Ingrese el nombre: ')
#         cedula=int(input('Ingrese la cedula: '))
#         genero=input('Ingrese el genero: ')
#         servicio=input('Ingrese el servicio: ')
        
#         p= Paciente()
#         p.AsignarNombre(nombre)
#         p.AsignarCedula(cedula)
#         p.AsignarGenero(genero)
#         p.AsignarServicio(servicio)
        
#         self.__ListaPacientes.append(p)
#         self.__NumeroPacientes= len(self.__ListaPacientes)
       
        
#     def VerNumeroPaciente(self): 
#         return self.__NumeroPacientes
    
    
#     def VerDatosPaciente(self):
#         cedula=int(input('Ingrese la cedula a buscar: '))
#         for paciente in self.__ListaPacientes: 
#             if cedula==paciente.VerCedula():
#                 print('Nombre: ' + paciente.VerNombre())
#                 print('Cedula: ' + str(paciente.VerCedula()))
#                 print('Genero: ' + paciente.VerGenero())
#                 print('Servicio: ' + paciente.VerServicio())


# mi_sistema=Sistema()
# while True: 
#     op=int(input('''Ingrese una opcion: 
#                  1. Nuevo paciente
#                  2. Numero de pacientes 
#                  3. Datos de pacientes
#                  4. Salir
#                  '''))
#     if op==1:
#         mi_sistema.IngresarPaciente()
#     elif op==2:
#         print(f'Ahora hay {mi_sistema.VerNumeroPaciente()} ingresados en el sistema')
#     elif op==3: 
#         mi_sistema.VerDatosPaciente()
#     elif op==4:
#         break 
#     else:
#         print('Opcion no valida, intente de nuevo.')