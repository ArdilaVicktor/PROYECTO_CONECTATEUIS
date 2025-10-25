# -----------------------------------------------------------
# ConectateUIS - Versión corregida 
# -----------------------------------------------------------
# Autor: David Santiago Sandoval Mancilla - 2242009
# Luiggy Ivan Rios Enrique - 2243166
# Maria Alejandra Hernandez Perez - 2242001
# Vicktor Josué David Ardila Carreño - 2230266
# -----------------------------------------------------------

from bigtree import Node, print_tree, plot_tree, findall

# -----------------------------------------------------------
# Ayudita: función para buscar un nodo por nombre (case-insensitive)
# Esta función hace lo que antes hacía find_node_by_name:
# busca por node.name o por node.data["nombre"] si existe.
# -----------------------------------------------------------
def buscar_nodo_por_nombre(raiz, nombre):
    nombre = nombre.strip().lower()
    # findall devuelve una lista de nodos que cumplen la condición
    nodos = findall(raiz, lambda n: (
        (isinstance(n.name, str) and n.name.lower() == nombre) or
        (hasattr(n, "data") and isinstance(n.data, dict) and str(n.data.get("nombre", "")).lower() == nombre)
    ))
    return nodos[0] if nodos else None

# -----------------------------------------------------------
# buscar por ID (IDs en data['id'], convertimos a str por seguridad)
# -----------------------------------------------------------
def buscar_nodo_por_id(raiz, id_buscar):
    id_s = str(id_buscar).strip().lower()
    nodos = findall(raiz, lambda n: (
        hasattr(n, "data") and isinstance(n.data, dict) and str(n.data.get("id", "")).lower() == id_s
    ))
    return nodos[0] if nodos else None

# -----------------------------------------------------------
# Creamos la raíz 
# -----------------------------------------------------------
campus = Node("Campus Principal", data={
    "id": 0,
    "nombre": "Campus Principal",
    "tipo": "Raíz",
    "descripcion": "Centro del sistema",
    "accesible": True,
    "conexiones": []
})

# -----------------------------------------------------------
# Funciones principales 
# -----------------------------------------------------------

def agregar_principal(data):
    """Agrega un nodo principal (hijo directo de la raíz)."""
    # Creamos con name = data['nombre'] y guardamos todo en data
    Node(data["nombre"], data=data, parent=campus)
    print(f" Nodo principal '{data['nombre']}' agregado al campus.\n")


def conectar_nodos(nombre_padre, data_hijo):
    """Conecta un nodo hijo bajo un padre existente (jerárquico)."""
    padre = buscar_nodo_por_nombre(campus, nombre_padre)
    if padre is None:
        print(f" El nodo '{nombre_padre}' no existe.\n")
        return

    hijo = Node(data_hijo["nombre"], data=data_hijo, parent=padre)
    # Guardamos la conexión (lista de ids) en el data del padre
    if isinstance(padre.data, dict):
        padre.data.setdefault("conexiones", []).append(data_hijo["id"])
    print(f" Se agregó '{data_hijo['nombre']}' como hijo de '{nombre_padre}'.\n")


def mostrar_estructura():
    """Imprime el árbol con la jerarquía."""
    print("\n🔹 Estructura actual del campus:\n")
    # print_tree usa node.name para mostrar, y como los nodos tienen name definido queda bonito
    print_tree(campus)
    print()


def buscar_por_nombre(nombre):
    nodo = buscar_nodo_por_nombre(campus, nombre)
    if nodo:
        d = nodo.data if isinstance(nodo.data, dict) else {}
        print(f"\n Encontrado: {d.get('nombre', nodo.name)} ({d.get('tipo', 'N/D')}) - accesible: {d.get('accesible', 'N/D')}\n")
        return nodo
    else:
        print("\n No se encontró el nodo.\n")
        return None


def buscar_por_id_func(id_buscar):
    nodo = buscar_nodo_por_id(campus, id_buscar)
    if nodo:
        d = nodo.data
        print(f"\n Nodo con ID {d.get('id')}: {d.get('nombre')} ({d.get('tipo')})\n")
        return nodo
    else:
        print("\n❌ No se encontró ningún nodo con ese ID.\n")
        return None


def listar_accesibles():
    """Muestra los nodos marcados accesibles en todo el árbol."""
    print("\n Lugares accesibles del campus:")
    encontrados = False
    for nodo in list(campus.descendants):  # convertimos a lista para iterar seguro
        if isinstance(nodo.data, dict) and nodo.data.get("accesible"):
            print(f" - {nodo.data.get('nombre')}")
            encontrados = True
    if not encontrados:
        print("⚠️ No hay nodos accesibles registrados.")
    print()


def buscar_ruta(origen, destino):
    """Busca ruta jerárquica simple entre dos nodos: sube hasta ancestro común y baja."""
    nodo_origen = buscar_nodo_por_nombre(campus, origen)
    nodo_destino = buscar_nodo_por_nombre(campus, destino)

    if not nodo_origen or not nodo_destino:
        print("\n Uno o ambos lugares no existen.\n")
        return

    # Construimos listas de ascendencia (incluye el nodo mismo)
    anc_origen = [nodo_origen] + list(nodo_origen.ancestors)
    anc_destino = [nodo_destino] + list(nodo_destino.ancestors)

    # Buscamos primer ancestro común (el más cercano a los nodos)
    ancestro_comun = None
    for a in anc_origen:
        if a in anc_destino:
            ancestro_comun = a
            break

    print("\n Ruta sugerida:")
    if ancestro_comun:
        # construir ruta: origen -> ... -> ancestro -> ... -> destino
        subida = [n.data.get("nombre", n.name) for n in anc_origen if n != ancestro_comun and n not in anc_destino]
        # ponemos ancestro
        medio = ancestro_comun.data.get("nombre", ancestro_comun.name)
        bajada = []
        # desde ancestro hasta destino (tomamos anc_destino hasta ancestro y la invertimos)
        ruta_dest_hasta_anc = []
        for n in anc_destino:
            ruta_dest_hasta_anc.append(n)
            if n == ancestro_comun:
                break
        # ruta desde ancestro hacia destino (excluimos ancestro y revertimos)
        ruta_down = list(reversed([n for n in ruta_dest_hasta_anc if n != ancestro_comun]))
        bajada = [n.data.get("nombre", n.name) for n in ruta_down]

        ruta_final = subida + [medio] + bajada
        print(" → ".join(ruta_final) + "\n")
    else:
        print("❌ No hay conexión jerárquica directa entre esos nodos.\n")


def mostrar_visual():
    """Muestra el árbol en modo texto bonito (sin abrir navegador)."""
    print("\n Visual del campus (texto):\n")
    print_tree(campus)
    print()


# -----------------------------------------------------------
# Menú 
# -----------------------------------------------------------
def menu():
    while True:
        print("\n===== MENÚ DEL CAMPUS =====")
        print("1. Agregar edificio o punto principal")
        print("2. Conectar nodo (Padre → Hijo)")
        print("3. Mostrar estructura jerárquica")
        print("4. Buscar por nombre")
        print("5. Buscar por ID")
        print("6. Listar accesibles")
        print("7. Buscar ruta entre lugares")
        print("8. Mostrar árbol visual (modo texto)")
        print("9. Salir")

        opcion = input("\nElige una opción (1-9): ").strip()

        if opcion == "1":
            # Pedimos todos los datos 
            id_nuevo = len(list(campus.descendants)) + 1  # convertir generator a lista
            nombre = input("Nombre del nuevo edificio o zona: ").strip()
            tipo = input("Tipo: ").strip()
            descripcion = input("Descripción: ").strip()
            accesible = input("¿Es accesible? (s/n): ").strip().lower() == "s"
            data = {"id": id_nuevo, "nombre": nombre, "tipo": tipo,
                    "descripcion": descripcion, "accesible": accesible, "conexiones": []}
            agregar_principal(data)

        elif opcion == "2":
            padre = input("Nombre del nodo padre: ").strip()
            nombre = input("Nombre del nodo hijo: ").strip()
            tipo = input("Tipo del hijo: ").strip()
            descripcion = input("Descripción: ").strip()
            accesible = input("¿Es accesible? (s/n): ").strip().lower() == "s"
            id_nuevo = len(list(campus.descendants)) + 1
            data = {"id": id_nuevo, "nombre": nombre, "tipo": tipo,
                    "descripcion": descripcion, "accesible": accesible, "conexiones": []}
            conectar_nodos(padre, data)

        elif opcion == "3":
            mostrar_estructura()

        elif opcion == "4":
            nombre = input("Nombre del lugar a buscar: ").strip()
            buscar_por_nombre(nombre)

        elif opcion == "5":
            id_buscar = input("ID a buscar: ").strip()
            buscar_por_id_func(id_buscar)

        elif opcion == "6":
            listar_accesibles()

        elif opcion == "7":
            origen = input("Lugar de origen: ").strip()
            destino = input("Lugar de destino: ").strip()
            buscar_ruta(origen, destino)

        elif opcion == "8":
            mostrar_visual()

        elif opcion == "9":
            print("\n Saliendo del sistema de rutas... ¡Hasta la próxima, bro!\n")
            break
        else:
            print("\n Opción no válida.\n")


# -----------------------------------------------------------
# Arranque
# -----------------------------------------------------------
if __name__ == "__main__":
    print(" Bienvenido al sistema de rutas del campus universitario.")
    menu()

