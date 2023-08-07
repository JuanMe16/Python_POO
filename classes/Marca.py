class Marca:
    __nombre: str
    __nacionalidad: str
    __precio: float

    def __init__(self, nombre: str, nacionalidad: str, precio: int):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__precio = precio

    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_nacionalidad(self) -> str:
        return self.__nacionalidad
    
    def get_precio(self) -> float:
        return self.__precio
    
    def set_nombre(self, nombre) -> None:
        self.__nombre = nombre

    def set_nacionalidad(self, nacionalidad) -> None:
        self.__nacionalidad = nacionalidad

    def set_precio(self, precio) -> None:
        self.__precio = precio

    def es_gama_alta(self) -> bool:
        return True if self.__precio > 300000000 else False

    def __str__(self) -> str:
        return f'La marca {self.__nombre} de {self.__nacionalidad} con precio ${self.__precio}'