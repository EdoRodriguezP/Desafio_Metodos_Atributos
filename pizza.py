from ingredientes import ingredientes_proteicos, ingredientes_vegetales, tipos_masa

class Pizza:
    # Atributos de clase
    precio = 10000
    tamaño = "Familiar"
    
    @classmethod
    def validar_elemento(cls, elemento, valores_posibles):
        """
        Método de clase que valida si un elemento está en una lista de valores posibles
        """
        return elemento in valores_posibles

    def __init__(self):
        self.ingrediente_proteico = None
        self.ingredientes_vegetales = []
        self.tipo_masa = None
        self.es_valida = False

    def realizar_pedido(self):
        """
        Método para realizar un pedido de pizza solicitando ingredientes al usuario
        """
        # Solicitar ingrediente proteico
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico ([pollo]/[vacuno]/[carne vegetal]: ")
        
        # Solicitar primer ingrediente vegetal
        vegetal1 = input("Ingrese el primer ingrediente vegetal [tomate]/[aceitunas]/[champiñones]: ")
        
        # Solicitar segundo ingrediente vegetal
        vegetal2 = input("Ingrese el segundo ingrediente vegetal [tomate]/[aceitunas]/[champiñones]: ")
        
        self.ingredientes_vegetales = [vegetal1, vegetal2]
        
        # Solicitar tipo de masa
        self.tipo_masa = input("Ingrese el tipo de masa [tradicional]/[delgada]: ")
        
        # Se validan los ingredientews
        proteico_valido = self.validar_elemento(self.ingrediente_proteico, ingredientes_proteicos)
        vegetales_validos = all(self.validar_elemento(v, ingredientes_vegetales) for v in self.ingredientes_vegetales)
        masa_valida = self.validar_elemento(self.tipo_masa, tipos_masa)
        
        # Se actualiza el estado de validez
        self.es_valida = proteico_valido and vegetales_validos and masa_valida
