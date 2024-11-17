# Función para controlar que la opción introducida por el usuario sea un número entero
def pedirOpc():
    while True:
        try:
            # Se solicita al usuario una opción y se guarda como entero.
            valor = int(input("Elige una opción: "))
            return valor # Devuelve el valor si es válido (es un número entero)
        except ValueError:
            # Si ocurre un error, pide al usuario que introduzca de nuevo un número.
            print("Opción incorrecta. Introduce de nuevo:")

#Funcion para mostrar los productos disponibles
def mostrarproductos():
    descripcion = 0  # Posición de la "descripción" dentro de la lista de atributos de los productos
    precio = 1  # Posición del "precio" dentro de la lista de atributos de los productos
    print("\n*** PRODUCTOS DISPONIBLES ***:")
    # Se comprueba si el diccionario de productos no está vacío
    if productos:
        for id_producto, valor in productos.items():
            # Muestra los datos de cada producto en stock (ID del producto, su descripción y su precio con 2 decimales)
            print(f"Id: {id_producto} | {valor[descripcion]} | {valor[precio]:.2f}€")
    else:
        print("\n No hay productos en stock.")
        # Mensaje para el caso en que no haya productos
        # Esta comprobación en verdad no sería necesaria, porque en este caso concreto se inicializa
        # el diccionario de productos al comienzo del programa en el propipo código.

#Función para mostrar carrito
def mostrarcarrito():
    print("\n*** CARRITO ***")
    # Se verifica si el carrito contiene productos
    if carrito:
        for id_producto, unidades in carrito.items():
            # Muestra la información de cada producto en el carrito
            print(f"Id: {id_producto} | {productos[id_producto][descripcion]} | {unidades} ud. | {productos[id_producto][precio]}€/ud | Subtotal: {productos[id_producto][precio] * unidades:.2f}€")
        # Se muestra el importe total actual del carrito.
        print(f"Total carrito: {total_compra:.2f}€")
    else:
        # Mensaje para cuando el carrito se encuentre vacío
        print("\nEl carrito está vacío.")

# Diccionarios para almacenar productos (inicializado con algunos productos), clientes y compras
productos = {
    1:["Cuaderno espiral",5.99],
    2:["Boligrafo BIC",0.50],
    3:["Lápiz",0.20],
    4:["Goma",0.75],
    5:["Sacapuntas",1.50]
}
clientes={} # Diccionario vacío para almacenar clientes
compras ={}  # Diccionario vacío para almacenar las compras
id_pedido = 1 # Inicializa el número de pedido en 1, con el fin de que, con cada pedido registrado, se vaya incrementando

opc=0 # Variable para entrar la primera vez en el siguiente bucle principal

while opc!=6: # El bucle se ejecuta hasta que el usuario elija la opción 6 (Salir)
    print("\n*** MENÚ ***")
    print("1. Registrar cliente.")
    print("2. Mostrar listado clientes.")
    print("3. Buscar cliente.")
    print("4. Realizar compra.")
    print("5. Seguimiento de compra.")
    print("6. Salir.")

    opc=pedirOpc() # Solicita una opción al usuario (llamando a la función definida al comienzo "pedirOpc")

    match opc:
        case 1:
            # Registro de cliente: se pedirán sus datos personales. Cada cliente debe tener un campo único (DNI).
            print("\n*** REGISTRAR CLIENTE ***")
            # Se solicita el DNI del cliente al usuario
            DNI_Cliente = (input("DNI_Cliente: "))
            # Se comprueba que el cliente no exista ya (que no haya un DNI registrado igual)
            if DNI_Cliente not in clientes:
                #Si no hay un cliente registrado con el DNI introducido se piden los siguientes datos:
                nombre_cliente = (input("Nombre: "))
                telefono = int(input("Teléfono: "))
                mail = input("Email: ")
                # Se almacena los datos solicitados en el diccionario
                clientes[DNI_Cliente] = [nombre_cliente,telefono, mail]
                print("\nRegistro de cliente realizado correctamente.")
            else:
                # Si el cliente ya está registrado (el DNI ya existe en el diccionario) se avisa con un mensaje.
                print("\nYa existe un cliente registrado con ese DNI .")
        case 2:
            print("\n*** MOSTRAR LISTADO DE CLIENTES ***")
            if clientes: # Se comprueba si hay clientes registrados
                for DNI_Cliente in sorted(clientes): # Se muestra los registros de clientes que hay ordenados por DNI
                    nombre, telefono, mail = clientes[DNI_Cliente]
                    print(f"DNI_Cliente: {DNI_Cliente} | Nombre: {nombre} | Telefono: {telefono} | E-Mail: {mail}")
            else:
                # Si no hay clientes se avisa con un mensaje.
                print("No hay clientes registrados.\n")
        case 3:
            print("\n*** BUSCAR CLIENTE ***")
            DNI_Cliente=input("DNI del cliente: ") # Se pide el DNI del cliente, que es el dato que se usará para buscar
            # Se comprueba si existe el DNI introducido en el diccionario de "clientes"
            if DNI_Cliente in clientes:
                nombre, telefono, mail = clientes [DNI_Cliente]
                print(f"DNI_Cliente: {DNI_Cliente} | Nombre: {nombre} | Telefono: {telefono} | E-Mail: {mail}")
            else:
                print(f"El cliente {DNI_Cliente} no consta como registrado.")
        case 4:
            print("\n*** REALIZAR COMPRA ***")
            carrito = {} # Se inicializa el carrito como vacío, para que cada nueva compra se comience con el carrito vacío
            total_compra = 0.0 # Se inicializa el importe total del carrio a 0, ya que se comienza con él vacío.

            # Pide el DNI del cliente, porque más adelante se guarda en la compra confirmada para asociarla al cliente
            DNI_cliente = input("Introduce DNI del cliente: ")
            # Se comprueba si el cliente está registrado
            if DNI_cliente not in clientes:
                print(f"El cliente {DNI_cliente} no consta como registrado.")
            else:
            # Si el cliente consta como registrado se le da la bienvenida con su nombre, y podrá entrar al siguiente bucle
            # Ya que cumplirá la condición de éste.
                print("\nBienvenid@ ", clientes[DNI_cliente][0])

            opc_compra = 0 # Se inicializa la opción del menú a 0 para que entre por primera vez al siguiente bucle.

            while (opc_compra!=5) and (DNI_cliente in clientes):
                # Se muestra el stock de productos que hay guardados en el diccionario productos,
                # a través de la función "mostrarproductos()" inicializada al comienzo del código.
                mostrarproductos()

                print("\n*** OPCIONES DE COMPRA ***")
                print("1. Añadir producto al carrito.")
                print("2. Eliminar producto del carrito.")
                print("3. Confirmar compra del carrito.")
                print("4. Ver carrito.")
                print("5. Volver al menú principal.")

                opc_compra=pedirOpc() # Solicita una opción al usuario (llamando a la función definida al comienzo "pedirOpc")

                match opc_compra: # Según la opción introducida se realizará un bloque de código u otro.
                    case 1:
                        print("\n*** AÑADIR PRODUCTO AL CARRITO ***")
                        id_producto = int(input("Id del producto: "))  # Se pide el ID del producto que desea comprar
                        if id_producto in productos:
                            descripcion = 0  # posicion de la "descripción" dentro de la lista atributos de los productos
                            precio = 1  # posicion del "precio" dentro de la lista de atributos de los productos

                            unidades = -1 # se inicializa en -1 para que entre una primera vez en el bucle while
                            # siguiente
                            # Bucle hasta que se ingrese una cantidad de unidades válida (mayor que 0)
                            while unidades <= 0:
                                unidades = int(input(f"Unidades: ")) # Pide la cantidad de unidades
                                if unidades <=0:
                                    # Se muestra un mensaje de error solo si la cantidad introducida es inválida
                                    print("ERROR: La cantidad debe ser un número positivo.\nPor favor, ingresa un valor válido.")
                            # Cuando la cantidad introducida es válida, se continua.
                            # Se comprueba si la id del producto ya está introducida en el carrito.
                            if id_producto in carrito:
                                # Se añade las unidades al carrito, acumulandolas si ya está en el carrito dicho producto
                                carrito[id_producto] = carrito[id_producto] + unidades
                            else:
                                # Si no está dicho producto, se añade el producto y las unidades que desea
                                carrito[id_producto] = unidades
                            # Se actualiza el importe total de la compra al haber añadido productos nuevos o más unidades.
                            total_compra = total_compra + productos[id_producto][precio] * unidades
                            # Se muestra un mensaje informando de la acción llevada a cabo.
                            print(f"Añadidas {unidades} ud. de {productos[id_producto][descripcion]} al carrito. ({productos[id_producto][precio]}€/ud)")
                        else:
                            #Si no hay productos con la id introducida, se avisa con un mensaje en pantalla.
                            print(f"No hay ningún producto con id {id_producto}.")

                        mostrarcarrito() # Se muestra el carrito actualizado después de añadir productos

                    case 2:
                        print("\n*** ELIMINAR PRODUCTO AL CARRITO ***")
                        id_producto = int(input("Id del producto: ")) # Se solicita el id del producto que desea eliminar
                        # Se comprueba si el producto está en el carrito
                        if id_producto in carrito:
                            unidades = int(input(f"Unidades a eliminar: ")) # Se solicita las unidades que quiere eliminar
                            # Se comprueba si las unidades supera las que hay en el carrito.
                            # Si las supera, se elimina el producto en sí, sino, solo las unidades que ha indicado el usuario.
                            if unidades >= carrito[id_producto]:
                                del carrito[id_producto]
                                print(f"Se ha eliminado el producto {productos[id_producto][descripcion]} del carrito.")
                            else:
                                carrito[id_producto] = carrito[id_producto] - unidades
                                print(f"Eliminadas {unidades} unidades de {productos[id_producto][descripcion]} del carrito.")
                            total_compra = total_compra - productos[id_producto][precio] * unidades  # Se actualiza el total del carrito
                        else:
                            # Si no hay productos con la id introducida se avisa por mensaje
                            print("Producto no encontrado en el carrito.")

                    case 3:
                        print("*** CONFIRMAR COMPRA DEL CARRITO")
                        # Se muestra el carrito actual ( a través de la función "mostrarcarrito()") para que
                        # el usuario pueda estar seguro de que desea confirmar la compra.
                        mostrarcarrito()
                        confirmar_carrito = input("¿Confirmar pedido del carrito actual? (S/N): ")

                        #Se comprueba si está vacío. Si está vacío se avisa de que no es posible confirmar la compra.
                        if total_compra <= 0:
                            print("\nNo hay ningún producto en el carrito. \nNo es posible confirmar compra.")
                        else:
                            if confirmar_carrito == "S":
                                # Si el carrito tiene productos añadidos, se guarda el pedido en "compras"
                                compras[id_pedido] = [DNI_cliente, carrito, total_compra]
                                print(f"Compra confirmada, {clientes[DNI_cliente][0]}.\nNúmero de pedido: #{id_pedido}")
                                id_pedido = id_pedido+1  # Se incrementa la variable contador de pedidos registrados.
                                # Se actualiza el carrito y el importe total de éste por si quiere añadir de nuevo
                                # productos al carrito sin volver al menú principal de la aplicación.
                                carrito={}
                                total_compra = 0.0
                            elif confirmar_carrito=="N": # Si elige no confirmar, se avisa de que no se ha llevado a cabo.
                                print("Confirmación cancelada.")
                            else:
                                # Si la opción introducida no es S ni N, se muestra un mensaje.
                                print("ERROR: Opción incorrecta")
                    case 4:
                        mostrarcarrito() # Se llama a la función "mostrarcarrito()" que ya realiza esta funcionalidad.
                    case 5:
                        print("Has elegido volver al menú principal.") # Se avisa de la opción escogida
                    case _:
                        print("ERROR: Opción incorrecta.") # Se avisa de que la opción introducida no existe en el menú.
        case 5:
            print("\n*** SEGUIMIENTO DE COMPRA ***")
            # Se solicita al usuario que introduzca el ID del pedido (se le mostró a la hora de confirmar el pedido)
            idpedido = int(input("Introduce el número de pedido: "))

            # Se comprueba si el ID de pedido introducido existe en el diccionario de compras
            if idpedido in compras:
                # Se recuperan los datos del pedido DNI del cliente, carrito y el importe total del pedido guardándola
                # en variables que se van a utilizar para mostrar un mensaje con estos datos
                DNI_cliente, carrito, total_pedido = compras[idpedido]
                # Se recupera también los datos del cliente asociado al pedido a partir del DNI
                nombre, telefono, mail = clientes[DNI_cliente]
                # Se muestra los detalles del pedido y cliente asociado a éste
                print(f"\nPedido Nº {idpedido} | DNI Clinete: {DNI_cliente} | Cliente: {nombre}")
                print(f"\nDetalles del pedido:")

                # Se muestra los productos del carrito que se compró en dicho pedido con su descripción,
                # cantidad y precio total por producto
                for id_productos, unidades in carrito.items():
                    descripcion, precio = productos[id_productos]
                    print(f"{descripcion} | Unidades: {unidades} | Precio: {precio} |Precio total: {precio * unidades:.2f}€")
                # Se muestra también el importe total del pedido con 2 decimales.
                print(f"Total del pedido: {total_pedido:.2f} €")
            else:
                # Si no consta ningún pedido con dicho número, se avisa por mensaje.
                print(f"No consta ningún Nº de pedido #{idpedido} realizado.")
        case 6:
            # Se avisa con un mensaje al usuario de que ha elegido salir del programa, antes de que se finalice el proceso.
            print("Has elegido salir del programa.")
        case _:
            # Se avisa al usuario de que la opción introducida no existe en el menú principal.
            print("ERROR: Opción incorrecta.")