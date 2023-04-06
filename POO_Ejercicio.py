
# Crear una clase Producto con los siguientes atributos:
#   -codigo
#   -nombre
#   -precio
# Crear su constructor, getter y setter y 
# una funcion(metodo) llamada calculo_total donde le pasaremos las unidades y nos debe calcular el precio final.


class Producto:

    def __init__(self, codigo, nombre, precio):
        
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        self.__precio = valor
    
    def __str__(self):
        return "Codigo: " + str(self.__codigo) + ", Nombre: " + str(self.__nombre) + ", Precio: $" + str(self.__precio)
    
    def calcular_total(self, unidades):
        return self.__precio * unidades


P1 = Producto(1,"prod_1",5)
P2 = Producto(2,"prod_2",15)
P3 = Producto(3,"prod_3",25)
P4 = Producto(3,"prod_4",7)

print(P2.calcular_total(5))

#añadir una clase pedido que tiene como atributos: 
# -lista de productos 
# -lista de cantidades 
# Añadir las funionalidades: 
# -total_pedido: muestra el precio final del pedido 
# -mostrar_productos: muestra los productos del pedido

class Pedido:

    def __init__ (self, productos, cantidades):
        self.__productos = []
        self.__cantidades = []

    def aniadir_producto(self, producto, cantidad):
        
        if not isinstance (producto, Producto):
            raise Exception ("Añadir producto: producto debe corresponder a la clase Producto.")

        if not isinstance (cantidad, int):
            raise Exception ("Añadir producto: cantidad debe ser un numero.")

        if cantidad <= 0:
            raise Exception ("Añadir producto: cantidad debe ser mayor a cero")
        
        if producto in self.__productos:
            indice = self.__productos.index(producto)
            self.__cantidades[indice] = self.__cantidades[indice] + cantidad
        else:
            self.__productos.append(producto)
            self.__cantidades.append(cantidad)


    def eliminar_producto(self, producto):

        if not isinstance (producto, Producto):
            raise Exception ("Eliminar producto: producto debe corresponder a la clase Producto.")

        if producto in self.__productos:
            indice = self.__productos.index(producto)
            del self.__productos[indice]
            del self.__cantidades[indice]
        else:
            raise Exception ("Eliminar producto: producto no existe")


    def total_pedido(self):
        total = 0

        for (p,c) in zip(self.__productos,self.__cantidades):
            total = total + p.calcular_total(c)

        return total

    def mostrar_pedido(self):

        for (p,c) in zip(self.__productos,self.__cantidades):
            print("Producto -> ",p.nombre," Cantidad -> ",str(c))


#productos = [P1,P2,P3,P4]
#cantidades = [2,5,3,1]

pedido = Pedido("P0",1)

try:

    pedido.aniadir_producto(P1,5)
    pedido.aniadir_producto(P2,6)
    pedido.aniadir_producto(P3,9)
    pedido.aniadir_producto(P4,1)
    pedido.aniadir_producto(P2,1)

    print("Total pedido :" + str(pedido.total_pedido()))

    pedido.mostrar_pedido()

    pedido.eliminar_producto(P1)

    print("Total pedido :" + str(pedido.total_pedido()))

    pedido.mostrar_pedido()   

except Exception as e:
    print(e)



print("Total pedido: " + str(pedido.total_pedido()))

pedido.mostrar_pedido()




