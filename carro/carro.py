# carro/carro.py

# Definición de la clase carro para realizar operaciones como agregar, eliminar un producto...
class Carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        #else:
        self.carro=carro
    
    # función para agregar un producto
    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else: #SI EL ARTICULO YA ESTA SE VA A INCREMENTAR
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1 #se va incrementando en uno
                    value["precio"] = float(value["precio"])+producto.precio
                    break
        self.guardar_carro()

    # Función para guardar el producto al carro
    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True
    
    #Eliminar un producto
    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    
    #eliminar unidades
    def restar_productos(self, producto):
        for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]-1 #se va restando en uno
                    value["precio"] = float(value["precio"])-producto.precio
                    if value["cantidad"]<1: #si es menor de uno eliminar el producto
                        self.eliminar(producto)
                    break
        self.guardar_carro()
    
    #limpiar el carrito
    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True
        
