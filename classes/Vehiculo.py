from .Marca import Marca

class Vehiculo:
    __placa: str
    __modelo: int
    __marca: Marca

    def __init__ (self, placa: str, modelo: int, marca: Marca):
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca

    def get_placa(self) -> str:
        return self.__placa
    
    def get_modelo(self) -> int:
        return self.__modelo
    
    def set_placa(self, placa: str) -> None:
        self.__placa = placa

    def set_modelo(self, modelo: int) -> None:
        self.__modelo = modelo

    def obtener_valorization(self) -> float:
        return self.__marca.__precio*0.95

    def __str__(self) -> str:
        return f'El vehiculo {self.__placa} de la marca {self.__marca.get_nombre()} con precio {self.__marca.get_precio()} tiene un modelo {self.__modelo}'