
"""
CARDINALIDAD
1..*  uno o varios
0 cero
1 uno
* varios


El diagrama muestra las siguientes entidades y relaciones:

Clases principales:
Cliente, Pedido, Linea Pedido, Producto, Vendedor, Tarjeta Crédito, Contrato, Sistema de Pago.


#####HHerencia (Generalización/Especialización):
Línea continua con un triángulo blanco NO RELLENO (la punta del triángulo es hueca).
Significado: Indica que la clase que tiene la base del triángulo hereda de la clase a
la que apunta la punta del triángulo ("es un tipo de").
la clase Cliente tiene el tringulo blanco con relleno es la clase padre

Cliente Personal      "hereda de"           Cliente.
1                  linea recta continua     triangulo blanco NO RELLENO apunta a Cliente 1

Cliente Corporativo   "hereda de"           Cliente.
1                  linea recta continua     triangulo blanco NO RELLENO  apunta a Cliente 1

#####Asociaciones:
Cliente        "realiza"      Pedido 
1      linea recta continua    1..*
(uno a muchos: un cliente realiza muchos pedidos). 

Pedido                "consta de"       Linea Pedido
1   rombo negro RELLENO   liena recta continua   1..*
(uno a muchos: un pedido tiene muchas líneas de pedido).


Linea Pedido        "formado por"      Producto
0   rombo blanco    linea recta continua      1..*   
(uno a uno: una línea de pedido se refiere a un producto).

Cliente Corporativo "atendido por" Vendedor 
*           liena recta continua   1
(muchos a uno: muchos clientes corporativos son atendidos por un vendedor).

Cliente Personal  "usa como medio de pago"      Tarjeta Crédito
1                 linea recta continua         1 
(uno a uno: un cliente personal usa una tarjeta de crédito).

Cliente Corporativo "usa como medio de pago" Contrato 
1                 linea recta continua         1 
(uno a uno: un cliente corporativo usa un contrato).


Dependencia/Uso:
Tarjeta Crédito "usa" Sistema de Pago
ERROR  linea recta continua  trinagulo blanco NO RELLENO que apunta a Sistema de Pago
DEBERIA SER  una linea discontinua de Tarjeta de Credito a usa/depende (flecha apunta a ) Sistema de PAgo

Contrato "usa" Sistema de Pago
ERROR liena recta continua  trinagulo blanco NO RELLENO que apunta a Sistema de Pago
DEBERIA SER  una linea discontinua de Contrato a usa/depende (flecha apunta a ) Sistema de Pago

Vendedor a Sistema de pago
(mostrado con una línea discontinua y flecha que se dirige Sistema de pago ).
Significado: Indica que una clase usa o depende de otra.
-Un cambio en la interfaz de la clase apuntada(Sistema de Pago)
podría afectar a la clase que la usa.(Vendedor)-



diferencia entre flecha y trinagulo blanco relleno

Línea recta continua con triángulo blanco no relleno (
Cliente Personal _______> Cliente,
Cliente Corporativo _______> Cliente):

Línea discontinua con flecha abierta (
Vendedor --> Sistema de Pago,
Tarjeta Crédito --> Sistema de Pago,
Contrato --> Sistema de Pago):
"""

# --- Clases Base ---

class Cliente:
    def __init__(self, id_cliente, nombre, direccion):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        self.pedidos = []  # Relación Cliente -> Pedido (uno a muchos)

    def realizar_pedido(self, pedido):
        """Asociación: Cliente realiza Pedido."""
        self.pedidos.append(pedido)

    def __str__(self):
        return f"Cliente(ID: {self.id_cliente}, Nombre: {self.nombre})"

class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto(ID: {self.id_producto}, Nombre: {self.nombre}, Precio: {self.precio:.2f}€)"

class Vendedor:
    def __init__(self, id_vendedor, nombre):
        self.id_vendedor = id_vendedor
        self.nombre = nombre

    def __str__(self):
        return f"Vendedor(ID: {self.id_vendedor}, Nombre: {self.nombre})"

class SistemaDePago:
    def __init__(self):
        pass # Podría tener métodos para procesar pagos

    def consultar_saldo(self): # Método indicado en el diagrama
        """Simula la consulta de saldo."""
        return 1000 # Ejemplo de saldo

    def procesar_pago(self, monto):
        """Simula el procesamiento de un pago."""
        print(f"Procesando pago de {monto:.2f}€ a través del Sistema de Pago.")
        return True

    def __str__(self):
        return "Sistema de Pago"

# --- Clases de Relación / Composición ---

class LineaPedido:
    def __init__(self, id_linea, producto, cantidad):
        self.id_linea = id_linea
        self.producto = producto  # Asociación: Linea Pedido -> Producto (referencia al objeto Producto)
        self.cantidad = cantidad
        self.subtotal = producto.precio * cantidad

    def __str__(self):
        return f"  Línea {self.id_linea}: {self.cantidad} x {self.producto.nombre} ({self.subtotal:.2f}€)"

class Pedido:
    def __init__(self, id_pedido, fecha, cliente):
        self.id_pedido = id_pedido
        self.fecha = fecha
        self.cliente = cliente # Asociación: Pedido -> Cliente (referencia al objeto Cliente)
        self.lineas_pedido = [] # Composición: Pedido --* Linea Pedido (uno a muchos)

    def agregar_linea(self, linea_pedido):
        """Asociación: Pedido consta de Línea Pedido."""
        self.lineas_pedido.append(linea_pedido)

    def calcular_total(self):
        return sum(linea.subtotal for linea in self.lineas_pedido)

    def __str__(self):
        lineas_str = "\n".join(str(lp) for lp in self.lineas_pedido)
        return (f"Pedido(ID: {self.id_pedido}, Fecha: {self.fecha}, Cliente: {self.cliente.nombre})\n"
                f"  Líneas:\n{lineas_str}\n"
                f"  Total: {self.calcular_total():.2f}€")

# --- Clases de Medios de Pago (Dependencia con SistemaDePago) ---

class TarjetaCredito:
    def __init__(self, numero, titular, fecha_exp):
        self.numero = numero
        self.titular = titular
        self.fecha_exp = fecha_exp
        self.sistema_pago = SistemaDePago() # Dependencia/Uso: TarjetaCredito usa SistemaDePago

    def pagar(self, monto):
        print(f"Usando Tarjeta de Crédito {self.numero}...")
        return self.sistema_pago.procesar_pago(monto)

    def consultar_saldo(self):
        return self.sistema_pago.consultar_saldo() # Llama al método del Sistema de Pago

    def __str__(self):
        return f"Tarjeta Crédito (Número: {self.numero}, Titular: {self.titular})"

class Contrato:
    def __init__(self, id_contrato, linea_credito):
        self.id_contrato = id_contrato
        self.linea_credito = linea_credito # Atributo específico del contrato
        self.sistema_pago = SistemaDePago() # Dependencia/Uso: Contrato usa SistemaDePago

    def pagar(self, monto):
        if monto <= self.linea_credito:
            print(f"Usando Contrato {self.id_contrato} (Línea de Crédito: {self.linea_credito})...")
            self.linea_credito -= monto # Reduce la línea de crédito disponible
            return self.sistema_pago.procesar_pago(monto)
        else:
            print(f"Crédito insuficiente para pagar {monto}€. Línea disponible: {self.linea_credito}.")
            return False

    def __str__(self):
        return f"Contrato (ID: {self.id_contrato}, Línea Crédito: {self.linea_credito})"

# --- Clases de Clientes (Herencia de Cliente) ---

class ClientePersonal(Cliente):
    def __init__(self, id_cliente, nombre, direccion, tarjeta_credito):
        super().__init__(id_cliente, nombre, direccion)
        self.tarjeta_credito = tarjeta_credito # Asociación: Cliente Personal -> Tarjeta Crédito

    def __str__(self):
        return f"Cliente Personal({super().__str__()}, Medio Pago: {self.tarjeta_credito.titular})"

class ClienteCorporativo(Cliente):
    def __init__(self, id_cliente, nombre, direccion, contrato, vendedor=None):
        super().__init__(id_cliente, nombre, direccion)
        self.contrato = contrato # Asociación: Cliente Corporativo -> Contrato
        self.vendedor = vendedor # Asociación: Cliente Corporativo -> Vendedor (opcional al inicio)

    def asignar_vendedor(self, vendedor):
        """Asociación: Cliente Corporativo atendido por Vendedor."""
        self.vendedor = vendedor

    def __str__(self):
        vendedor_info = f", Vendedor: {self.vendedor.nombre}" if self.vendedor else ""
        return f"Cliente Corporativo({super().__str__()}, Contrato: {self.contrato.id_contrato}{vendedor_info})"

# --- Ejemplos de uso y demostración de relaciones ---

print("--- Creación de Objetos ---")
# Productos
prod1 = Producto("P001", "Laptop", 1200.00)
prod2 = Producto("P002", "Teclado", 75.50)
prod3 = Producto("P003", "Ratón", 25.00)
print(prod1)
print(prod2)
print(prod3)

# Vendedor
vendedor1 = Vendedor("V001", "Juan Pérez")
print(vendedor1)

# Medios de Pago
tarjeta1 = TarjetaCredito("1111-2222-3333-4444", "Ana García", "12/26")
print(tarjeta1)
contrato1 = Contrato("C001", 10000.00) # Línea de crédito de 10,000€
print(contrato1)

# Clientes
cliente_personal1 = ClientePersonal("CP001", "Laura López", "Calle Falsa 123", tarjeta1)
print(cliente_personal1)
cliente_corp1 = ClienteCorporativo("CC001", "Empresa A S.L.", "Av. Principal 456", contrato1)
cliente_corp1.asignar_vendedor(vendedor1) # Asignamos el vendedor
print(cliente_corp1)


print("\n--- Realización de un Pedido ---")
# Un cliente personal realiza un pedido
pedido1 = Pedido("PED001", "2025-07-21", cliente_personal1)
linea1_ped1 = LineaPedido("LP001", prod1, 1) # 1 Laptop
linea2_ped1 = LineaPedido("LP002", prod2, 2) # 2 Teclados
pedido1.agregar_linea(linea1_ped1)
pedido1.agregar_linea(linea2_ped1)
cliente_personal1.realizar_pedido(pedido1) # El cliente "realiza" el pedido

print(pedido1)
print(f"Pedidos de {cliente_personal1.nombre}: {[p.id_pedido for p in cliente_personal1.pedidos]}")

print("\n--- Proceso de Pago ---")
# El cliente personal paga su pedido
print(f"Cliente personal {cliente_personal1.nombre} pagará {pedido1.calcular_total():.2f}€")
if cliente_personal1.tarjeta_credito.pagar(pedido1.calcular_total()):
    print("Pago con tarjeta exitoso.")
else:
    print("Pago con tarjeta fallido.")

print("\n--- Cliente Corporativo y su Contrato ---")
print(f"Cliente corporativo {cliente_corp1.nombre} pagará 1500€.")
if cliente_corp1.contrato.pagar(1500):
    print("Pago con contrato exitoso.")
    print(f"Nueva línea de crédito disponible: {cliente_corp1.contrato.linea_credito:.2f}€")
else:
    print("Pago con contrato fallido.")

print("\n--- Demostración de herencia ---")
print(f"¿{cliente_personal1.nombre} es una instancia de Cliente? {isinstance(cliente_personal1, Cliente)}")
print(f"¿{cliente_corp1.nombre} es una instancia de ClientePersonal? {isinstance(cliente_corp1, ClientePersonal)}")


"""
Explicación de las Relaciones en el Código:
Herencia (Generalización/Especialización):


ClientePersonal(Cliente) y ClienteCorporativo(Cliente): Se implementa usando la sintaxis class ClaseHija(ClasePadre): y llamando a super().__init__() en sus constructores. Esto significa que ClientePersonal y ClienteCorporativo son tipos específicos de Cliente y heredan sus atributos y comportamientos. 

Asociación (Uno a Muchos - Composición / Agregación):

Cliente "realiza" Pedido: Un Cliente tiene una lista de pedidos (self.pedidos = []) a la que se le añaden los objetos Pedido cuando el cliente los "realiza" (cliente.realizar_pedido(pedido)). Esto es una composición o agregación, ya que los pedidos "pertenecen" a un cliente.

Pedido "consta de" Linea Pedido: Un Pedido tiene una lista de lineas_pedido (self.lineas_pedido = []). Cuando se crea una LineaPedido, esta se asocia con un Producto, y luego se añade al Pedido (pedido.agregar_linea(linea_pedido)). Esto es una composición fuerte, ya que las líneas de pedido no existen sin un pedido.

Cliente Corporativo "atendido por" Vendedor: Un ClienteCorporativo tiene un atributo self.vendedor que guarda una referencia a un objeto Vendedor. Esto es una asociación, ya que Vendedor y ClienteCorporativo pueden existir independientemente.

Asociación (Uno a Uno / Referencia):

Linea Pedido "formado por" Producto: La clase LineaPedido tiene un atributo self.producto que directamente almacena una referencia a un objeto Producto. Una línea de pedido específica se refiere a un único producto.

Cliente Personal "usa como medio de pago" Tarjeta Crédito: ClientePersonal tiene un atributo self.tarjeta_credito que almacena una referencia a un objeto TarjetaCredito.

Cliente Corporativo "usa como medio de pago" Contrato: ClienteCorporativo tiene un atributo self.contrato que almacena una referencia a un objeto Contrato.

Dependencia/Uso (Relación de "usa"):

Tarjeta Crédito y Contrato "usan" Sistema de Pago: Ambas clases (TarjetaCredito y Contrato) crean una instancia de SistemaDePago (self.sistema_pago = SistemaDePago()) dentro de sus constructores y luego llaman a métodos de SistemaDePago (como procesar_pago o consultar_saldo). Esto indica que dependen de SistemaDePago para realizar ciertas operaciones, pero no "tienen" un SistemaDePago como parte de su estado fundamental, sino que lo utilizan para una tarea específica.
"""