class Producto:
 def _init_(self,nombre, precio, cantidad):
  self.nombre = nombre
  self.precio = precio
  self.cantidad = cantidad 

 # mostrar_info() → muestra los datos del producto
# valor_total() → devuelve precio × cantidad
def mostrar_info(self):
    print(f"nombre: {self.nombre}")
    print(f"precio: {self.precio}")
    print(f"cantidad: {self.cantidad}")

def valor_total(self):
  return self.precio*self.cantidad

productos = []
def agregar_productos():
  nombre = input("ingrese el nombre del producto")
  precio = float(input("ingrese el precio"))
  cantidad = int(input("ingrese la cantidad"))

nuevo_producto = Producto (nombre,precio,cantidad)
Producto.append(nuevo_producto)
print("producto agregado")

def mostra_productos():
  if len (productos) == 0:
    print("no hya productos registrador")
  else:
    for p in productos:
      print("---------------")
      p.mostrar_info()
      print("Valor total: ",p.valor_total())

while True:
 print("\n --MENU--")
 print("1. Agregar productos")
 print("2. Mostrar Productos")
 print("3. salir")

 opcion = input("elija una opcion: ") 
 if opcion == "1":