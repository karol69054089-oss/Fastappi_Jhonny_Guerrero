from pydantic import BaseModel, computed_field
from sqlmodel import SQLModel, Field, Relationship
from .transacciones import Transaccion
from .clientes import Cliente, ClienteLeer
from datetime import datetime






#Crear el modelo transacciones (id, fecha, vr_total, cliente)
class FacturaBase(SQLModel):
    fecha: str = Field(default=datetime.now())
    #cliente: Cliente # esta es la relacion con el cliente(objeto)
    #transacciones: list[Transaccion] = []

    @computed_field
    @property
    def vr_total (self) -> float:
        total_factura = 0.0
        if self.transacciones == None:
            return total_factura
        # #recorrer la lista transacciones, segun el factura_id
        for transaccion in self.transacciones:
            total_factura += transaccion.vr_unitario * transaccion.cantidad
        return total_factura
    

class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(FacturaBase):
    pass


class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(default=None, foreign_key="cliente.id")
    #crear relaciones virtuales con cliente, transacciones - NO en la BD
    cliente : Cliente = Relationship(back_populates="factura")
    transacciones: list[Transaccion] = Relationship(back_populates="factura")


#crea modelo para mostrar al usuario o el cliente
class FacturaLeer(FacturaBase):
    id: int
    cliente: ClienteLeer
    #pero no es recomendable, por las buenas practicas
    #transacciones: list[Transaccion] = []

class FacturaLeerCompuesta(FacturaLeer):
    transacciones: list[Transaccion] = []