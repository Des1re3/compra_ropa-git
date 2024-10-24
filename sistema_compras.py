class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre  # Atributo público
        self.precio = precio  # Atributo público
        self.cantidad = cantidad  # Atributo público

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.cantidad}")

class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de la clase padre
        self.talla = talla  # Atributo específico de RopaHombre

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre
        print(f"Talla: {self.talla}")

camisa = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
pantalon = RopaHombre("Pantalón de Hombre", 30.00, 30, "32")
chaqueta = RopaHombre("Chaqueta de Hombre", 55.00, 20, "M")
zapatos_hombre = RopaHombre("Zapatos de Hombre", 60.00, 25, "42")   


class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")

falda = RopaMujer("Falda de Mujer", 28.00, 15, "S")
blusa = RopaMujer("Blusa de Mujer", 22.00, 40, "S") 
vestido = RopaMujer("Vestido de Mujer", 45.00, 10, "S") 
zapatos_mujer = RopaMujer("Zapatos de Mujer", 50.00, 20, "36")          


class Inventario:
    def __init__(self):
        self.prendas = []  # Lista para almacenar las prendas
        self.carrito = [] 

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)  # Agrega la prenda a la lista

    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()  # Muestra la información de cada prenda


    def agregar_al_carrito(self):
        while True:
            nombre_prenda = input("Ingrese el nombre de la prenda que desea agregar (o escriba 'finalizar compra' para terminar): ").lower()
            if nombre_prenda == 'finalizar compra':
                break
            for prenda in self.prendas:
                if prenda.nombre.lower() == nombre_prenda:
                    self.carrito.append(prenda)
                    print(f"Se agregó {prenda.nombre} al carrito.")
                    break
            else:
                print("La prenda no se encuentra en el inventario.")

    def mostrar_carrito(self):
        print("Contenido del carrito:")
        for prenda in self.carrito:
            prenda.mostrar_info()

    def procesar_compra(self):
        print("¡Compra procesada con éxito!")

       
inventario = Inventario()
inventario.agregar_prenda(camisa)
inventario.agregar_prenda(pantalon)
inventario.agregar_prenda(chaqueta)
inventario.agregar_prenda(zapatos_hombre)
inventario.agregar_prenda(falda)    
inventario.agregar_prenda(blusa)
inventario.agregar_prenda(vestido)
inventario.agregar_prenda(zapatos_mujer) 
inventario.mostrar_inventario()

inventario.agregar_al_carrito()
inventario.mostrar_carrito()
inventario.procesar_compra()
    