# Abrir base de dados
with open(r'teste.txt', 'r') as arq:
    dados = arq.read()

# Tratamento inicial
dados = dados.replace(" - ;", "")
dados = dados.replace(" -", "")
dados = dados.replace(" - ", "")
dados = dados.replace("- ", "")
dados = dados.replace(" ;", ";")
dados = dados.replace("\n", "")
dados = dados.replace(" ", "")

# print(dados)
# Criando uma lista com os dados
candidatos = dados.split('/')
for i in range(len(candidatos)):
    candidatos[i] = candidatos[i].split(';')

keys = ['Nome', 'Num', 'nota', 'num2']

lista_nomes = []
lista_num = []
lista_nota = []
lista_num2 = []

# Criando uma lista capaz de ser convertida para dicionário
for i, item in enumerate(candidatos):
    for j in range(len(item)):
        match j:
            case 0:
                lista_nomes.append(candidatos[i][j])
            case 1:
                lista_num.append(candidatos[i][j])
            case 2:
                lista_nota.append(candidatos[i][j])
            case 3:
                lista_num2.append(candidatos[i][j])

candidatos_lista = [lista_nomes, lista_num, lista_nota, lista_num2]

# Criando dicionário
dicio_Candidatos = dict(zip(keys, candidatos_lista))

# print(dicio_Candidatos)

# Mostrando dados
print(sorted(dicio_Candidatos['num2']))
print(type(dicio_Candidatos))
