from pizza import Pizza

# Se muestran los atributos de clase
print(f"Precio de la pizza: ${Pizza.precio}")
print(f"Tamaño de la pizza: {Pizza.tamaño}")

# Validar si "salsa de tomate" está en la lista
resultado = Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"])
print(f"¿[salsa de tomate] está en la lista?: {resultado}")

# Se crea instancia y realizar pedido
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# Se muestran detalles de la pizza seleccionada
print("\nDetalles de tu pizza:")
print(f"Ingrediente proteico: {mi_pizza.ingrediente_proteico}")
print(f"Ingredientes vegetales: {', '.join(mi_pizza.ingredientes_vegetales)}")
print(f"Tipo de masa: {mi_pizza.tipo_masa}")
print(f"¿Es una pizza válida?: {mi_pizza.es_valida}")

# Intentar acceder al atributo es_valida de la clase pero esto generará un error.
print(f"¿La clase Pizza es válida?: {Pizza.es_valida}")  
