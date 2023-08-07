from classes.VehiculoParticular import VehiculoParticular
from classes.VehiculoPublico import VehiculoPublico
from classes.Vehiculo import Vehiculo
from classes.Marca import Marca
from typing import List
import pickle
import os

class main:
    lista_vehiculos: List[Vehiculo]

    def __init__(self):
        self.lista_vehiculos = []
        print('¡Bienvenido a la aplicación!')
        try:
            archivo_guardado = open('datos_guardados', 'rb+')
            self.lista_vehiculos = pickle.load(archivo_guardado)
            print(f'Se cargaron datos del archivo de guardado.')
            archivo_guardado.close()
            del(archivo_guardado)
        except Exception:
            open('datos_guardados','x')
            print('Fichero vacio')

    def __guardar_informacion(self) -> None:
        archivo_guardado = open('datos_guardados', 'wb')
        pickle.dump(self.lista_vehiculos, archivo_guardado)
        archivo_guardado.close()
        del(archivo_guardado)

    def añadir_vehiculo(self) -> None:
        try:
            tipo_vehiculo = int(input('Tipo de vehiculo | (1) Publico | (2) Particular | '))
            placa = input('Digite la placa del vehiculo | ')
            modelo = int(input('Digite el modelo del vehiculo | '))
            dueño = input('Digite el propietario o la empresa dueña del vehiculo | ')

            nombre_marca = input('Digite el nombre de la marca | ')
            nacionalidad_marca = input('Digite la nacionalidad de la marca | ')
            precio = int(input('Digite el precio | $'))
        except ValueError as verr:
            return print('Hubo un error en los datos digitados',verr)
        
        if tipo_vehiculo == 1:
            vehiculo = VehiculoPublico(placa, modelo, Marca(nombre_marca, nacionalidad_marca, precio), dueño)
        elif tipo_vehiculo == 2:
            vehiculo = VehiculoParticular(placa, modelo, Marca(nombre_marca, nacionalidad_marca, precio), dueño)
        else:
            return print('Error: Valor invalido para el tipo de vehiculo.')
        
        self.lista_vehiculos.append(vehiculo)
        self.__guardar_informacion()

    def listar_vehiculos(self) -> None:
        for vehiculo in self.lista_vehiculos:
            print(f'{self.lista_vehiculos.index(vehiculo)}) {vehiculo}')

    def eliminar_vehiculo(self) -> None:
        self.listar_vehiculos()
        vehiculo_a_eliminar = int(input('Digite el numero del vehiculo a eliminar | '))
        if vehiculo_a_eliminar > len(self.lista_vehiculos) or vehiculo_a_eliminar < 0:
            return print('Error: numero de vehiculo inexistente.')
        del self.lista_vehiculos[vehiculo_a_eliminar]
        self.__guardar_informacion()

if __name__ == '__main__':
    os.system('cls')
    executed_module = main()

    while True:

        try:
            user = int(input('Menu | (1) Añadir vehiculo | (2) Eliminar vehiculo | (3) Listar vehiculos | (4) Salir | '))
        except:
            user = 5

        if user == 1:
            executed_module.añadir_vehiculo()
        elif user == 2:
            executed_module.eliminar_vehiculo()
        elif user == 3:
            executed_module.listar_vehiculos()
        elif user == 4:
            print('Saliendo...')
            break
        else:
            print('Inserte un valor correcto del menu')
            continue