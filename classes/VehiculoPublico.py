from .Vehiculo import Vehiculo
from .Marca import Marca

class VehiculoPublico(Vehiculo):
    __empresa: str

    def __init__(self, placa: str, modelo: str, marca: Marca, empresa: str):
        super().__init__(placa, modelo, marca)
        self.__empresa = empresa

    def set_empresa(self, empresa: str) -> None:
        self.__empresa = empresa

    def get_empresa(self) -> str:
        return self.__empresa

    def obtener_valorization(self) -> float:
        return self.__marca.__precio*0.98
    
    def obtener_año_renovacion(self) -> int:
        return self.__modelo+20

    def __str__(self):
        return super().__str__() + f' perteneciente a la empresa {self.__empresa}'