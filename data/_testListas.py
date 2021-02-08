# Se genera la lista a modificar
estaLista = ["a", "b", "c", "d", [1, 2, 3, 4, 5], "e", "f", "g"]

# MUESTRA la lista
print(estaLista)

# Quita el item pedido de la lista
# elDato = estaLista.pop(4)
elDato = estaLista[4].pop(3)

# MUESTRA el item eliminado de la lista y el nuevo estado de la lista
print(elDato)
print(estaLista)

# Agrega el dato en la lista
largoLista = len(estaLista)
# estaLista.insert(5, elDato)
estaLista.insert(largoLista, elDato)

# MUESTRA el item eliminado de la lista y el nuevo estado de la lista
print(elDato)
print(estaLista)