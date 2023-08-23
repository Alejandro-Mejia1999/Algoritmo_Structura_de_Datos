from ArbolBinario import*  # Importa la clase del otro archivo

arbol = ArbolBinario()

arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(8)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(7)
arbol.insertar(9)

# Puedes agregar más valores aquí

# Imprime el árbol en orden
def imprimir_inorden(nodo):
    if nodo is not None:
        imprimir_inorden(nodo.izquierda)
        print(nodo.valor, end=" ")
        imprimir_inorden(nodo.derecha)

print("Árbol ordenado:")
imprimir_inorden(arbol.raiz)
