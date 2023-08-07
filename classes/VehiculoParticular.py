from .Vehiculo import Vehiculo
from .Marca import Marca

class VehiculoParticular(Vehiculo):
    __propietario: str

    def __init__(self, placa: str, modelo: int, marca: Marca, propietario: str):
        super().__init__(placa, modelo, marca)
        self.__propietario = propietario

    def get_propietario(self) -> str:
        return self.__propietario
    
    def set_propietario(self, propietario: str) -> None:
        self.__propietario = propietario

    def obtener_valorization(self) -> float:
        return self.__marca.__precio*0.80
    
    def __str__(self) -> str:
        return super().__str__() + f' perteneciente a {self.__propietario}'