import random as r

lista_de_lista_de_inteiros = []

# Escolher o número de listas internas
for i in range(r.randint(5, 10)):
    lista_de_lista_de_inteiros.append([])

# Preencher as listas internas
for i in range(len(lista_de_lista_de_inteiros)):
    for num in range(10):
        lista_de_lista_de_inteiros[i].append(r.randint(1, 10))

# Mostrar lista gerada
print(f"\nLista gerada: ")

for i in range(len(lista_de_lista_de_inteiros)):
    print(lista_de_lista_de_inteiros[i])

# Procura pela primeira ocorrência de duplicados, caso não ache retorne -1
primeiro_Duplicado = -1
for i in range(len(lista_de_lista_de_inteiros)):
    for j in range(len(lista_de_lista_de_inteiros[i])-1):
        if lista_de_lista_de_inteiros[i][j] == lista_de_lista_de_inteiros[i][j+1]:
            primeiro_Duplicado = lista_de_lista_de_inteiros[i][j]
            break
    else:  # Este else é executado caso o for interno corra normalmente
            # (sem ter executado o primeiro break)
        continue
    break  # Se o else não for executado, esse break para a varredura

print(f"\nA primeira duplicada foi {primeiro_Duplicado}")
